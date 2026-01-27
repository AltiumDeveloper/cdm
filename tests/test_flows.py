import pytest
import common_data_model.datamodel.common_data_model as cdm
from tests.clients.esd_client import ESDClient
from .clients.e2_client import E2Client
from .sim import SIM

def test_sim_flow():
    """Happy path scenario - ESD updates SIM first, adding a new functional block, e2 studio pulls the latest
    version and adds a new software component."""

    sim = SIM.empty()

    # ----------------------
    # Domain: functional
    # Tool: ESD
    # ----------------------

    # Connect mock ESD client to SIM instance
    esd = ESDClient()
    esd.pull_from_sim(sim)

    # Make changes to ESD model
    esd.model.functionalBlocks.append(cdm.SystemFunctionalBlock(
      id="unique_block_id",
      name="MCU",
      keyComponents=[
        cdm.SystemKeyComponent(id="unique_key_component_id", name="R7FA6M5AG2CBG"),
      ],
      ports=[
        cdm.SystemPort(id="unique_port_id", name="UART")
      ]
    ))

    esd.configure_device(cdm.DmConfiguredDeviceModel(
      id="unique_device_id",
      mpn="R7FA6M5AG2CBG"
    ))

    # Push ESD changes back to SIM
    esd.push_to_sim(sim)

    # Dump SIM state to the console
    sim.dump()

    # ----------------------
    # Domain: software
    # Tool: e2 studio
    # ----------------------

    # Connect mock ESD client to SIM instance
    e2 = E2Client()
    e2.pull_from_sim(sim)

    # Make changes to ESD model
    e2.model.components.append(cdm.SftSoftwareComponent(
        id="unique_software_component_id",
        vendor="Renesas",
        name="FSP driver",
        version="1.2.0"
    ))

    # Push ESD changes back to SIM
    e2.push_to_sim(sim)

    # Dump SIM state to the console
    sim.dump()

def test_concurrent_sim_updates():
    """Simulating a scenario when two clients (esd, e2) try to push updates
    to the same baseline versio of SIM. The first one succeeds, the second one fails, prompting to
    pull the latest changes first and perform an ECO"""

    sim = SIM.empty()
    assert sim.version == 0

    # Connect mock clients to SIM instance
    esd = ESDClient()
    esd.pull_from_sim(sim)
    assert esd.baseline.version == 0

    e2 = E2Client()
    e2.pull_from_sim(sim)
    assert e2.baseline.version == 0

    # Make changes to ESD model and push the changes
    esd.model.functionalBlocks.append(cdm.SystemFunctionalBlock(
      id="unique_block_id",
      name="MCU",
      keyComponents=[
        cdm.SystemKeyComponent(id="unique_key_component_id", name="R7FA6M5AG2CBG"),
      ],
      ports=[
        cdm.SystemPort(id="unique_port_id", name="UART")
      ]
    ))
    esd.push_to_sim(sim)
    assert sim.version == 1
    assert esd.baseline.version == 1

    # Make changes to ESD model
    e2.model.components.append(cdm.SftSoftwareComponent(
        id="unique_software_component_id",
        vendor="Renesas",
        name="FSP driver",
        version="1.2.0"
    ))

    # Push ESD changes back to SIM - should fail as SIM has a newer version
    with pytest.raises(Exception) as ex:
        e2.push_to_sim(sim)
        assert ex