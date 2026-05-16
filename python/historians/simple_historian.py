"""
HydroTurbine-SCADA
Simple Industrial Historian
"""

import csv
import time
import random
from datetime import datetime

from python.plc_comm.plc_tags import PELTON_TAGS


# ---------------------------------------------------
# HISTORIAN CLASS
# ---------------------------------------------------

class SimpleHistorian:

    def __init__(self):

        self.filename = "pelton_historical_data.csv"

        self.tags = PELTON_TAGS

        self.initialize_csv()

    # -------------------------------------------------

    def initialize_csv(self):

        try:

            with open(self.filename, mode="x", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "timestamp",
                    "rpm",
                    "flow",
                    "pressure",
                    "power"
                ])

            print(f"[OK] Historian file created: {self.filename}")

        except FileExistsError:

            print(f"[INFO] Historian file already exists")

    # -------------------------------------------------

    def acquire_data(self):

        return {

            "rpm": round(random.uniform(400, 950), 2),

            "flow": round(random.uniform(15, 45), 2),

            "pressure": round(random.uniform(1.5, 6.0), 2),

            "power": round(random.uniform(50, 350), 2)

        }

    # -------------------------------------------------

    def save_data(self):

        data = self.acquire_data()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.filename, mode="a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([

                timestamp,

                data["rpm"],

                data["flow"],

                data["pressure"],

                data["power"]

            ])

        print("-----------------------------------")

        print(f"Timestamp: {timestamp}")

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
        print("Simple Historian")
        print("===================================")

        while True:

            self.save_data()

            time.sleep(2)


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

if __name__ == "__main__":

    historian = SimpleHistorian()

    historian.run()