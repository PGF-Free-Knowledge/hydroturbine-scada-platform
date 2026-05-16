"""
HydroTurbine-SCADA
Live Console Dashboard
"""

import csv
import os
import time


HISTORIAN_FILE = "pelton_historical_data.csv"


# ---------------------------------------------------
# CLEAR SCREEN
# ---------------------------------------------------

def clear_console():

    os.system("cls" if os.name == "nt" else "clear")


# ---------------------------------------------------
# READ LAST DATA
# ---------------------------------------------------

def read_last_row():

    try:

        with open(HISTORIAN_FILE, mode="r") as file:

            reader = list(csv.DictReader(file))

            if len(reader) == 0:

                return None

            return reader[-1]

    except Exception as e:

        print("[ERROR] Historian read failed")
        print(e)

        return None


# ---------------------------------------------------
# DASHBOARD LOOP
# ---------------------------------------------------

while True:

    clear_console()

    print("===================================")
    print("HydroTurbine-SCADA")
    print("Pelton Live Dashboard")
    print("===================================")

    data = read_last_row()

    if data:

        print("\nIndustrial Variables:\n")

        print(f"RPM            : {data['rpm']}")
        print(f"FLOW           : {data['flow']}")
        print(f"PRESSURE       : {data['pressure']}")
        print(f"POWER          : {data['power']}")

        print(f"\nLAST UPDATE    : {data['timestamp']}")

        print("\nSystem Status  : RUNNING")

    else:

        print("\nNo historian data available")

    time.sleep(2)