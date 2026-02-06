import uuid
from copy import deepcopy
from typing import Dict, Any

import common_data_model.datamodel.common_data_model as cdm


class IdMapper:
    def __init__(self, name: str) -> None:
        self.counter = 1
        self.name = name
        self.mapping: dict[str, str] = {}

    def map_id(self, original_id: str) -> str:
        try:
            return self.mapping[original_id]
        except KeyError:
            self.mapping[original_id] = "guid-" + str(self.counter)
            self.counter += 1
            return self.mapping[original_id]

    def map_entity(self, entity: Any) -> Any:
        original_id = entity.id
        entity.id = self.map_id(entity.id)
        entity.metadata = [
            cdm.SystemSmClientMetadata(
                clientId=self.name,
                parameters=[cdm.SystemParameter(id="local-id", value=original_id)],
            )
        ]
        return entity


class ESDClient:
    def __init__(
        self,
        model: cdm.SystemESDDocument = None,
        latest_sdm: cdm.SystemSystemModel = None,
    ) -> None:
        self.model = model if model else cdm.SystemESDDocument(id="esd-1")
        self.latest_sdm = (
            latest_sdm
            if latest_sdm
            else cdm.SystemSystemModel(
                id="sdm-1",
                version=0,
                functionalModel=None,
                deviceModels=[],
                softwareModels=[],
                hardwareModels=[],
            )
        )
        self.deviceModels: Dict[str, cdm.SystemSmDeviceModel] = {}
        self.sw_library: Dict[str, cdm.SystemSmSoftwareSpecification] = {}
        self.id_mapper = IdMapper(name="esd")

    def add_sw_library_item(
        self,
        name: str,
        vendor: str,
        ecosystem: str,
        package_name: str,
        category: cdm.SystemSmSoftwareComponentCategory,
    ) -> str:
        self.sw_library[name] = cdm.SystemSmSoftwareSpecification(
            name=package_name,
            vendor=vendor,
            ecosystem=ecosystem,
            category=category,
        )
        return name

    def add_functional_block(
        self, title: str, hw_project: cdm.SystemHardwareProject | None
    ) -> cdm.SystemFunctionalBlock:
        """Helper to add a functional block to the ESD model"""
        block = cdm.SystemFunctionalBlock(
            id=f"fb-{len(self.model.functionalBlocks) + 1}", name=title
        )
        self.model.functionalBlocks.append(block)
        if hw_project:
            hw_project.functionalBlocks.append(block.id)
        return block

    def add_hardware_project(self, implemented_by: str = None):
        """Helper to add a hardware project to the ESD model"""
        project = cdm.SystemHardwareProject(
            id=f"hp-{len(self.model.hardwareProjects) + 1}",
            implementedBy=implemented_by,
        )
        self.model.hardwareProjects.append(project)
        return project

    def add_software_project(self, implemented_by: str = None):
        """Helper to add a software project to the ESD model"""
        project = cdm.SystemSoftwareProject(
            id=f"sp-{len(self.model.softwareProjects) + 1}",
            implementedBy=implemented_by,
        )
        self.model.softwareProjects.append(project)
        return project

    def add_hardware_component(
        self, block: cdm.SystemFunctionalBlock, mpn: str
    ) -> cdm.SystemKeyComponent:
        """Helper to add a key-component to a functional block in the ESD model"""
        component = cdm.SystemKeyComponent(
            id=f"{block.id}.kc-{len(block.keyComponents) + 1}", name=mpn
        )
        block.keyComponents.append(component)
        return component

    def add_software_component(
        self,
        block: cdm.SystemFunctionalBlock,
        key_comp: cdm.SystemKeyComponent,
        name: str,
        sft_project: cdm.SystemSoftwareProject,
    ) -> cdm.SystemSoftwareComponent:
        """Helper to add a key-component to a functional block in the ESD model"""
        component = cdm.SystemSoftwareComponent(
            id=f"{block.id}.sc-{len(block.keyComponents) + 1}",
            name=name,
            parentKeyComponentId=key_comp.id,
        )
        block.softwareComponents.append(component)
        sft_project.softwareComponents.append(component.id)
        return component

    def add_port(
        self,
        block: cdm.SystemFunctionalBlock,
        port_type: cdm.SystemPortType,
        name: str = None,
    ) -> cdm.SystemPort:
        """Helper to add a port to a functional block in the ESD model"""
        port = cdm.SystemPort(
            id=f"port-{len(block.ports) + 1}",
            name=name or port_type.text,
            parameters=[
                cdm.SystemParameter(id="param-1", name="Type", value=port_type.text),
            ],
        )
        block.ports.append(port)
        return port

    def add_connection(
        self,
        src_block: cdm.SystemFunctionalBlock,
        src_port: cdm.SystemPort,
        dst_block: cdm.SystemFunctionalBlock,
        dst_port: cdm.SystemPort,
    ):
        """Helper to add connectivity between two functional blocks in the ESD model"""
        connection = cdm.SystemConnection(
            id=f"conn-{len(self.model.connections) + 1}",
            endpoints=[
                cdm.SystemEndpoint(functionalBlockId=src_block.id, portId=src_port.id),
                cdm.SystemEndpoint(functionalBlockId=dst_block.id, portId=dst_port.id),
            ],
        )
        self.model.connections.append(connection)
        return connection

    def configure_device(
        self, hw_component: cdm.SystemKeyComponent, device: cdm.SystemSmDeviceModel
    ) -> None:
        """Simulate device configuration via (RA) Device Modeler"""
        self.deviceModels[hw_component.id] = device

    def compile_sdm(self):
        """Compile the System (Data) Model from the current ESD state"""
        # Fully replace functional model
        sdm = deepcopy(self.latest_sdm)
        sdm.id = self.id_mapper.map_id(self.latest_sdm.id)
        sdm.version = self.latest_sdm.version + 1
        if sdm.functionalModel is None:
            sdm.functionalModel = self.id_mapper.map_entity(cdm.SystemSmFunctionalModel(id=self.model.id))

        fb_blocks = dict()
        sw_components = dict()
        hw_components = dict()

        sdm.functionalModel.functionalBlocks = []
        for fb in self.model.functionalBlocks:
            fb_blocks[fb.id] = fb
            sdm.functionalModel.functionalBlocks.append(
                self.id_mapper.map_entity(
                    cdm.SystemSmFunctionalBlock(
                        id=fb.id,
                        name=fb.name,
                        hardwareComponentIds=[
                            self.id_mapper.map_id(x.id) for x in fb.keyComponents
                        ],
                        ports=[
                            self.id_mapper.map_entity(
                                cdm.SystemSmPort(
                                    id=p.id, name=p.name, parameters=p.parameters
                                )
                            )
                            for p in fb.ports
                        ],
                    )
                )
            )

            for sw_component in fb.softwareComponents:
                sw_components[sw_component.id] = sw_component
            for hw_component in fb.keyComponents:
                hw_components[hw_component.id] = hw_component

        for con in self.model.connections:
            sdm.functionalModel.connections.append(
                self.id_mapper.map_entity(
                    cdm.SystemSmConnection(
                        id=con.id,
                        endpoints=[
                            cdm.SystemSmEndpoint(
                                functionalBlockId=self.id_mapper.map_id(
                                    e.functionalBlockId
                                ),
                                portId=self.id_mapper.map_id(e.portId),
                            )
                            for e in con.endpoints
                        ],
                    )
                )
            )

        # Fully replace hardware model
        sdm.hardwareModels = []
        for hp in self.model.hardwareProjects:
            hw_model = cdm.SystemSmHardwareModel(
                id=hp.id,
                implementedBy=hp.implementedBy,
                hardwareComponents=[],
                functionalBlockIds=[],
            )

            for fbId in hp.functionalBlocks:
                hw_model.functionalBlockIds.append(self.id_mapper.map_id(fbId))
                for kc in fb_blocks[fbId].keyComponents:
                    hw_comp = cdm.SystemSmHardwareComponent(id=kc.id, name=kc.name)
                    if kc.id in self.deviceModels:
                        hw_comp.deviceModelId = self.id_mapper.map_id(
                            self.deviceModels[kc.id].id
                        )
                    hw_model.hardwareComponents.append(
                        self.id_mapper.map_entity(hw_comp)
                    )
            sdm.hardwareModels.append(self.id_mapper.map_entity(hw_model))

        # Fully replace software model
        sdm.softwareModels = []
        for sp in self.model.softwareProjects:
            sw_components = [sw_components[sc_id] for sc_id in sp.softwareComponents]

            sw_model = self.id_mapper.map_entity(
                cdm.SystemSmSoftwareModel(
                    id=sp.id,
                    implementedBy=sp.implementedBy,
                    softwareComponents=[
                        self.id_mapper.map_entity(
                            cdm.SystemSmSoftwareComponent(
                                id=sc.id,
                                name=sc.name,
                                specification=self.sw_library.get(sc.name, None),
                            )
                        )
                        for sc in sw_components
                    ],
                )
            )

            if sw_components:
                hw_component = sw_components[0].parentKeyComponentId
                # Add blank device model for hardware component if not already present
                if hw_component not in self.deviceModels:
                    self.deviceModels[hw_component] = cdm.SystemSmDeviceModel(
                        id=f"dm-{len(self.deviceModels) + 1}",
                        mpn=hw_components[hw_component].name,
                        peripherals=[],
                        ports=[],
                    )

                sw_model.deviceModelId = self.id_mapper.map_id(
                    self.deviceModels[hw_component].id
                )

            sdm.softwareModels.append(sw_model)

        # Fully replace device model
        sdm.deviceModels = []
        for dm in self.deviceModels.values():
            sdm.deviceModels.append(self.id_mapper.map_entity(dm))

        return sdm

    #
    # def push_to_sim(self, sim: SIM):
    #     SIMClient.ensure_up_to_date(sim, self.baseline)
    #
    #     # update SIM - trivial "full update" for now
    #     sim.update_functional_model(self.model)
    #     if self.device:
    #         sim.update_device_model(self.device)
    #
    #     # save the new baseline version of the SIM
    #     self.baseline = sim.snapshot()
    #
    # def pull_from_sim(self, sim: SIM):
    #     # TODO: perform ECO
    #
    #     # save the new baseline version of the SIM
    #     self.baseline = sim.snapshot()
