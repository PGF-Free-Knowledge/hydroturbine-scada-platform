# Este módulo generará señales operacionales simuladas de una turbina Pelton
# Inicialmente permitirá:

# generar RPM simuladas
# generar caudal simulado
# generar presión simulada
# generar torque simulado
# enviar datos periódicamente

# Posteriormente podrá integrarse con:

# Grafana
# Node-RED
# PostgreSQL
# InfluxDB
# APIs
# PLC Siemens
# OPC-UA
# MQTT

"""
HydroTurbine-SCADA
Pelton Turbine Industrial Simulator
"""

import time
import random

from python.plc_comm.plc_tags import PELTON_TAGS


# ---------------------------------------------------
# SIMULATION LOOP
# ---------------------------------------------------

print("===================================")
print("HydroTurbine-SCADA")
print("Pelton Industrial Simulator")
print("===================================")

print("\nLoaded PLC Tags:\n")

for tag, config in PELTON_TAGS.items():

    print(f"{tag} -> DB{config['db']} | BYTE {config['start']} | {config['type']}")

print("\nStarting industrial simulation...\n")


while True:

    simulated_data = {

        "rpm": round(random.uniform(400, 950), 2),

        "flow": round(random.uniform(15, 45), 2),

        "pressure": round(random.uniform(1.5, 6.0), 2),

        "power": round(random.uniform(50, 350), 2)

    }

    print("-----------------------------------")

    for tag, value in simulated_data.items():

        config = PELTON_TAGS[tag]

        print(
            f"{tag.upper()} | "
            f"DB{config['db']} | "
            f"BYTE {config['start']} | "
            f"VALUE = {value}"
        )

    time.sleep(2)