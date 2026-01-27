import common_data_model.datamodel.common_data_model as cdm
from tests.clients.sim_client import SIMClient
from tests.sim import SIM


class ESDClient(SIMClient):

    model: cdm.SystemESDDocument
    device: cdm.DmConfiguredDeviceModel = None

    baseline: SIM

    def __init__(self, model: cdm.SystemESDDocument = None) -> None:
        self.model = model if model else cdm.SystemESDDocument(id="unique_esd_id")

    def configure_device(self, device: cdm.DmConfiguredDeviceModel) -> None:
        """Simulate device configuration via (RA) Device Modeler"""
        self.device = device

    def push_to_sim(self, sim: SIM):
        SIMClient.ensure_up_to_date(sim, self.baseline)

        # update SIM - trivial "full update" for now
        sim.update_functional_model(self.model)
        if self.device:
            sim.update_device_model(self.device)

        # save the new baseline version of the SIM
        self.baseline = sim.snapshot()

    def pull_from_sim(self, sim: SIM):
        # TODO: perform ECO

        # save the new baseline version of the SIM
        self.baseline = sim.snapshot()
