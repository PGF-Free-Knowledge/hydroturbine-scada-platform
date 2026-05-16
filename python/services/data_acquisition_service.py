"""
HydroTurbine-SCADA
Industrial Data Acquisition Service
"""

import time
import random

from python.plc_comm.plc_tags import PELTON_TAGS


# ---------------------------------------------------
# DATA ACQUISITION SERVICE
# ---------------------------------------------------

class DataAcquisitionService:

    def __init__(self):

        self.tags = PELTON_TAGS

    # -------------------------------------------------

    def acquire_data(self):

        simulated_data = {

            "rpm": round(random.uniform(400, 950), 2),

            "flow": round(random.uniform(15, 45), 2),

            "pressure": round(random.uniform(1.5, 6.0), 2),

            "power": round(random.uniform(50, 350), 2)

        }

        return simulated_data

    # -------------------------------------------------

    def process_cycle(self):

        data = self.acquire_data()

        print("-----------------------------------")

        for tag, value in data.items():

            config = self.tags[tag]

            print(
                f"{tag.upper()} | "
                f"DB{config['db']} | "
                f"BYTE {config['start']} | "
                f"VALUE = {value}"
            )

    # -------------------------------------------------

    def run(self):

        print("===================================")
        print("HydroTurbine-SCADA")
        print("Data Acquisition Service")
        print("===================================")

        while True:

            self.process_cycle()

            time.sleep(2)


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

if __name__ == "__main__":

    service = DataAcquisitionService()

    service.run()