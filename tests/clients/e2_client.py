import common_data_model.datamodel.common_data_model as cdm
from tests.clients.sim_client import SIMClient
from tests.sim import SIM


class E2Client(SIMClient):

    model: cdm.SftSoftwareBom
    baseline: SIM

    def __init__(self, model: cdm.SftSoftwareBom = None) -> None:
        self.model = model if model else cdm.SftSoftwareBom(id="sbom-1", components=[])
        pass

    def push_to_sim(self, sim: SIM):
        SIMClient.ensure_up_to_date(sim, self.baseline)

        # update SIM - trivial "full update" for now
        sim.update_software_model(self.model)
        # save the new baseline version of the SIM
        self.baseline = sim.snapshot()

    def pull_from_sim(self, sim: SIM):
        # TODO: perform ECO

        # save the new baseline version of the SIM
        self.baseline = sim.snapshot()