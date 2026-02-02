from copy import deepcopy

import common_data_model.datamodel.common_data_model as cdm


class ESDClient:
    model: cdm.SystemESDDocument
    deviceModels: dict[str, cdm.DmConfiguredDeviceModel] = {}

    latest_sdm: cdm.SystemSystemModel

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
                functionalModel=None,
                deviceModels=[],
                softwareModels=[],
                hardwareModels=[],
            )
        )

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
            id=f"kc-{len(block.keyComponents) + 1}", name=mpn
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
            id=f"sc-{len(block.keyComponents) + 1}",
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
            name=name or port_type,
            parameters=[
                cdm.SystemParameter(id="param-1", name="Type", value=str(port_type)),
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
        self, hw_component: cdm.SystemKeyComponent, device: cdm.DmConfiguredDeviceModel
    ) -> None:
        """Simulate device configuration via (RA) Device Modeler"""
        self.deviceModels[hw_component.id] = device

    def compile_sdm(self):
        """Compile the System (Data) Model from the current ESD state"""
        # Fully replace functional model
        sdm = deepcopy(self.latest_sdm)
        if sdm.functionalModel is None:
            sdm.functionalModel = cdm.SystemSmFunctionalModel(id=self.model.id)

        sw_components = dict()
        hw_components = dict()

        sdm.functionalModel.functionalBlocks = []
        for fb in self.model.functionalBlocks:
            sdm.functionalModel.functionalBlocks.append(
                cdm.SystemSmFunctionalBlock(
                    id=fb.id,
                    name=fb.name,
                )
            )

            for sw_component in fb.softwareComponents:
                sw_components[sw_component.id] = sw_component
            for hw_component in fb.keyComponents:
                hw_components[hw_component.id] = hw_component

        for con in self.model.connections:
            sdm.functionalModel.connections.append(
                cdm.SystemSmConnection(
                    id=con.id,
                    endpoints=[
                        cdm.SystemSmEndpoint(
                            functionalBlock=e.functionalBlockId, port=e.portId
                        )
                        for e in con.endpoints
                    ],
                )
            )

        # Fully replace hardware model
        sdm.hardwareModels = []
        for hp in self.model.hardwareProjects:
            sdm.hardwareModels.append(
                cdm.SystemSmHardwareModel(
                    id=hp.id,
                    implementedBy=hp.implementedBy,
                    functionalBlocks=hp.functionalBlocks,
                )
            )

        # Fully replace software model
        sdm.softwareModels = []
        for sp in self.model.softwareProjects:
            sw_components = [sw_components[sc_id] for sc_id in sp.softwareComponents]

            sw_model = cdm.SystemSmSoftwareModel(
                id=sp.id,
                implementedBy=sp.implementedBy,
                softwareComponents=[
                    cdm.SystemSmSoftwareComponent(
                        id=sc.id,
                        name=sc.name,
                    )
                    for sc in sw_components
                ],
            )

            if sw_components:
                hw_component = sw_components[0].parentKeyComponentId
                # Add blank device model for hardware component if not already present
                if hw_component not in self.deviceModels:
                    self.deviceModels[hw_component] = cdm.SystemSmDeviceModel(
                        id=f"dm-{len(self.deviceModels) + 1}",
                        deviceMpn=hw_components[hw_component].name,
                        peripherals=[],
                    )
                sw_model.deviceModel = self.deviceModels[hw_component].id

            sdm.softwareModels.append(sw_model)

        # Fully replace device model
        sdm.deviceModels = []
        for dm in self.deviceModels.values():
            sdm.deviceModels.append(dm)

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
