from linkml_runtime.dumpers import json_dumper

from tests.clients.esd_client import ESDClient
import common_data_model.datamodel.common_data_model as cdm


def test_esd_client():
    esd = ESDClient()

    hw_project = esd.add_hardware_project()
    sw_project = esd.add_software_project()

    mcu = esd.add_functional_block(title="MCU", hw_project=hw_project)
    mcu_uart = esd.add_port(mcu, cdm.SystemPortType.UART)

    wifi_ble = esd.add_functional_block(title="WiFi + BLE", hw_project=hw_project)
    wifi_uart = esd.add_port(wifi_ble, cdm.SystemPortType.UART)

    _ = esd.add_connection(mcu, mcu_uart, wifi_ble, wifi_uart)

    mcu_hw_comp = esd.add_hardware_component(mcu, "R7FA6M3AH3CFB")
    _ = esd.add_hardware_component(wifi_ble, "DA16600MOD-AAE4WA32")

    _ = esd.add_software_component(mcu, mcu_hw_comp, "WiFi Common", sw_project)

    esd.configure_device(
        hw_component=mcu_hw_comp,
        device=cdm.DmConfiguredDeviceModel(
            id="device-1",
            mpn="R7FA6M3AH3CFB",
            peripherals=[
                cdm.DmPeripheral(
                    id="sci",
                    name="Connectivity:SCI",
                    instances=[
                        cdm.DmPeripheralInstance(
                            id="sci9",
                            name="SCI9",
                            unit="9",
                            modes=[
                                cdm.DmPeripheralMode(
                                    name="Asynchronous UART",
                                    configurations=[
                                        cdm.DmPeripheralConfiguration(
                                            id="sci9.mode.asynchronous.a",
                                            pinConfigs=[
                                                cdm.DmPeripheralPinConfig(
                                                    pinName="sci9.rxd",
                                                    pinValue="sci9.rxd.p202",
                                                    function="RXD",
                                                    portName="P202",
                                                ),
                                                cdm.DmPeripheralPinConfig(
                                                    pinName="sci9.txd",
                                                    pinValue="sci9.txd.p203",
                                                    function="TXD",
                                                    portName="P203",
                                                ),
                                            ],
                                            pinDependencyConfigs=[
                                                cdm.DmPeripheralPinDependencyConfig(
                                                    name="ci9.pairing",
                                                    value="sci9.pairing.a",
                                                ),
                                            ],
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                ),
            ],
            ports=[
                cdm.DmPort(
                    id="p202",
                    name="P202",
                    pin="46",
                    functions=[cdm.DmPortFunction(name="RXD_MISO")],
                ),
                cdm.DmPort(
                    id="p203",
                    name="P203",
                    pin="45",
                    functions=[cdm.DmPortFunction(name="TXD_MOSI")],
                ),
            ],
        ),
    )

    sdm = esd.compile_sdm()
    print("\n" + json_dumper.dumps(sdm, inject_type=False))


# def test_add_port_flow():
#     """Happy path scenario - ESD updates SIM first, adding a new functional block, e2 studio pulls the latest
#     version and adds a new software component."""
#
#     sdm =
#     sim = SIM.empty()
#
#     # ----------------------
#     # Domain: functional
#     # Tool: ESD
#     # ----------------------
#
#     # Connect mock ESD client to SIM instance
#     esd = ESDClient()
#     esd.pull_from_sim(sim)
#
#     # Add functional block with key-component and port to ESD model
#     esd.model.functionalBlocks.append(
#         cdm.SystemFunctionalBlock(
#             id="esd-1",
#             name="MCU",
#             keyComponents=[
#                 cdm.SystemKeyComponent(id="key-comp-1", name="R7FA6M3AH3CFB"),
#             ],
#             ports=[cdm.SystemPort(id="port-1", name="UART")],
#         )
#     )
#
#     # Set device model from Device Modeler output
#     esd.configure_device(
#         cdm.DmConfiguredDeviceModel(
#             id="device-1",
#             mpn="R7FA6M3AH3CFB",
#             peripherals=[
#                 cdm.DmPeripheral(
#                     id="sci",
#                     name="Connectivity:SCI",
#                     instances=[
#                         cdm.DmPeripheralInstance(
#                             id="sci9",
#                             name="SCI9",
#                             unit="9",
#                             modes=[
#                                 cdm.DmPeripheralMode(
#                                     name="Asynchronous UART",
#                                     configurations=[
#                                         cdm.DmPeripheralConfiguration(
#                                             id="sci9.mode.asynchronous.a",
#                                             pinConfigs=[
#                                                 cdm.DmPeripheralPinConfig(
#                                                     pinName="sci9.rxd",
#                                                     pinValue="sci9.rxd.p202",
#                                                     function="RXD",
#                                                     portName="P202",
#                                                 ),
#                                                 cdm.DmPeripheralPinConfig(
#                                                     pinName="sci9.txd",
#                                                     pinValue="sci9.txd.p203",
#                                                     function="TXD",
#                                                     portName="P203",
#                                                 ),
#                                             ],
#                                             pinDependencyConfigs=[
#                                                 cdm.DmPeripheralPinDependencyConfig(
#                                                     name="ci9.pairing",
#                                                     value="sci9.pairing.a",
#                                                 ),
#                                             ],
#                                         )
#                                     ],
#                                 )
#                             ],
#                         )
#                     ],
#                 ),
#             ],
#             ports=[
#                 cdm.DmPort(
#                     id="p202",
#                     name="P202",
#                     pin="46",
#                     functions=[cdm.DmPortFunction(name="RXD_MISO")],
#                 ),
#                 cdm.DmPort(
#                     id="p203",
#                     name="P203",
#                     pin="45",
#                     functions=[cdm.DmPortFunction(name="TXD_MOSI")],
#                 ),
#             ],
#         )
#     )
#
#     # Push ESD changes back to SIM
#     esd.push_to_sim(sim)
#
#     # Dump SIM state to the console
#     sim.dump()
#
#     # ----------------------
#     # Domain: software
#     # Tool: e2 studio
#     # ----------------------
#
#     # Connect mock ESD client to SIM instance
#     e2 = E2Client()
#     e2.pull_from_sim(sim)
#
#     # Make changes to ESD model
#     e2.model.components.extend(
#         [
#             cdm.SftSoftwareComponent(
#                 id="module.driver.uart_on_sci_uart.726871374",
#                 name="g_uart0",
#                 vendor="Renesas",
#                 version="6.2.0",
#                 dependencies=[
#                     "module.driver.transfer_on_dtc.1284901769",
#                     "module.driver.transfer_on_dtc.1593719623",
#                 ],
#             ),
#             cdm.SftSoftwareComponent(
#                 id="module.driver.transfer_on_dtc.1284901769",
#                 name="g_transfer0",
#                 vendor="Renesas",
#                 version="6.2.0",
#                 dependencies=[],
#             ),
#             cdm.SftSoftwareComponent(
#                 id="module.driver.transfer_on_dtc.1593719623",
#                 name="g_transfer0",
#                 vendor="Renesas",
#                 version="6.2.0",
#                 dependencies=[],
#             ),
#         ]
#     )
#
#     # Push ESD changes back to SIM
#     e2.push_to_sim(sim)
#
#     # Dump SIM state to the console
#     sim.dump()
#
#
# def test_concurrent_sim_updates():
#     """Simulating a scenario when two clients (esd, e2) try to push updates
#     to the same baseline versio of SIM. The first one succeeds, the second one fails, prompting to
#     pull the latest changes first and perform an ECO"""
#
#     sim = SIM.empty()
#     assert sim.version == 0
#
#     # Connect mock clients to SIM instance
#     esd = ESDClient()
#     esd.pull_from_sim(sim)
#     assert esd.baseline.version == 0
#
#     e2 = E2Client()
#     e2.pull_from_sim(sim)
#     assert e2.baseline.version == 0
#
#     # Make changes to ESD model and push the changes
#     esd.model.functionalBlocks.append(
#         cdm.SystemFunctionalBlock(
#             id="unique_block_id",
#             name="MCU",
#             keyComponents=[
#                 cdm.SystemKeyComponent(
#                     id="unique_key_component_id", name="R7FA6M5AG2CBG"
#                 ),
#             ],
#             ports=[cdm.SystemPort(id="unique_port_id", name="UART")],
#         )
#     )
#     esd.push_to_sim(sim)
#     assert sim.version == 1
#     assert esd.baseline.version == 1
#
#     # Make changes to ESD model
#     e2.model.components.append(
#         cdm.SftSoftwareComponent(
#             id="unique_software_component_id",
#             vendor="Renesas",
#             name="FSP driver",
#             version="1.2.0",
#         )
#     )
#
#     # Push ESD changes back to SIM - should fail as SIM has a newer version
#     with pytest.raises(Exception) as ex:
#         e2.push_to_sim(sim)
#         assert ex
