import copy
from pathlib import Path
from linkml_runtime.loaders import json_loader
from linkml_runtime.dumpers import json_dumper
import common_data_model.datamodel.common_data_model as cdm

def load_sim(filepath: str) -> cdm.SystemSim:
    return json_loader.load(filepath, target_class=cdm.SystemSim)

class SIM:
    _model: cdm.SystemSim
    version: int

    #region Fabric / ctors

    @staticmethod
    def empty():
        return SIM(model=cdm.SystemSim(id="unique_sim_id"))

    @staticmethod
    def from_json(filepath: Path):
        return SIM(model=load_sim(str(filepath)))

    def __init__(self, model: cdm.SystemSim = None):
        self._model = model
        self.version = 0

    #endregion

    def __repr__(self):
        return json_dumper.dumps(self._model)

    #region Update methods

    def update_functional_model(self, functional_model: cdm.SystemESDDocument):
        self.version += 1
        self._model.functionalModel = copy.deepcopy(functional_model)

    def update_software_model(self, software_model: cdm.SftSoftwareBom):
        self.version += 1
        self._model.softwareModels.append(copy.deepcopy(software_model))

    def update_device_model(self, device_model: cdm.DmConfiguredDeviceModel):
        self.version += 1
        self._model.deviceModels.append(copy.deepcopy(device_model))

    #endregion

    def snapshot(self):
        return copy.deepcopy(self)

    def dump(self):
        print(repr(self))