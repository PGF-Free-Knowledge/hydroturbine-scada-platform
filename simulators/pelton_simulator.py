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

import time
import random

print("=== Pelton Simulator iniciado ===")

while True:

    rpm = random.randint(400, 900)

    caudal = round(random.uniform(15.0, 40.0), 2)

    presion = round(random.uniform(1.5, 5.0), 2)

    torque = round(random.uniform(80.0, 250.0), 2)

    print("-----------------------------------")
    print(f"RPM: {rpm}")
    print(f"Caudal: {caudal} L/s")
    print(f"Presión: {presion} bar")
    print(f"Torque: {torque} Nm")

    time.sleep(2)