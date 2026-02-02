import os

from linkml_runtime.dumpers import json_dumper

from tests.clients.esd_client import ESDClient
import common_data_model.datamodel.common_data_model as cdm

def assert_sdm_matches_expected(sdm, expected_filepath: str):
    sdm_json = json_dumper.dumps(sdm, inject_type=False)
    print("SDM:\n" + sdm_json)
    print("")
    with open(os.path.join(os.path.dirname(__file__), expected_filepath)) as f:
        expected_json = f.read()
    assert sdm_json == expected_json

def test_esd_basic_flow():
    esd = ESDClient()

    hw_project = esd.add_hardware_project()
    sw_project = esd.add_software_project()

    wifi = esd.add_sw_library_item(
        name="WiFi",
        vendor="Renesas",
        ecosystem="FSP",
        package_name="module.driver.wifi_da16xxx",
        category=cdm.SystemSmSoftwareComponentCategory.DRIVER,
    )

    mcu = esd.add_functional_block(title="MCU", hw_project=hw_project)
    mcu_uart = esd.add_port(mcu, cdm.SystemPortType.UART)

    wifi_ble = esd.add_functional_block(title="WiFi + BLE", hw_project=hw_project)
    wifi_uart = esd.add_port(wifi_ble, cdm.SystemPortType.UART)

    _ = esd.add_connection(mcu, mcu_uart, wifi_ble, wifi_uart)

    mcu_hw_comp = esd.add_hardware_component(mcu, "R7FA6M3AH3CFB")
    _ = esd.add_hardware_component(wifi_ble, "DA16600MOD-AAE4WA32")

    _ = esd.add_software_component(mcu, mcu_hw_comp, wifi, sw_project)

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
    assert_sdm_matches_expected(sdm, "data/esd_basic_flow.json")
