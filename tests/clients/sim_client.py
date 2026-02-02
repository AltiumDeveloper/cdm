# from tests.sim import SIM
#
#
# class SIMClient:
#     baseline: SIM
#
#     def push_to_sim(self, sim: SIM):
#         pass
#
#     def pull_from_sim(self, sim: SIM):
#         pass
#
#     @staticmethod
#     def ensure_up_to_date(sim: SIM, baseline: SIM):
#         # Check if the current SIM version is the same as the baseline.
#         # If it is newer - pull has to happen first
#         if sim.version > baseline.version:
#             raise Exception(
#                 f"Current SIM version {baseline.version} does not match baseline version {sim.version}. Pull the changes first.")