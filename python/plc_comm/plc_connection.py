# Qué hace este módulo:
# crea cliente Siemens
# prepara conexión Ethernet
# prepara arquitectura Snap7
# permite conexión/desconexión
# estructura futura reutilizable

"""
HydroTurbine-SCADA
Siemens PLC Connection Module
"""

import snap7


class SiemensPLC:

    def __init__(self, ip, rack=0, slot=1):

        self.ip = ip
        self.rack = rack
        self.slot = slot

        self.client = snap7.client.Client()

    # -------------------------------------------------
    # CONNECT
    # -------------------------------------------------

    def connect(self):

        try:

            self.client.connect(
                self.ip,
                self.rack,
                self.slot
            )

            if self.client.get_connected():

                print(f"[OK] Connected to PLC: {self.ip}")

            else:

                print("[ERROR] PLC connection failed")

        except Exception as e:

            print("[EXCEPTION] Connection error")
            print(e)

    # -------------------------------------------------
    # DISCONNECT
    # -------------------------------------------------

    def disconnect(self):

        try:

            self.client.disconnect()

            print("[OK] PLC disconnected")

        except Exception as e:

            print("[EXCEPTION] Disconnect error")
            print(e)


# -------------------------------------------------
# TEST ENVIRONMENT
# -------------------------------------------------

if __name__ == "__main__":

    print("===================================")
    print("HydroTurbine-SCADA")
    print("PLC Connection Test")
    print("===================================")

    plc = SiemensPLC(
        ip="192.168.0.10",
        rack=0,
        slot=1
    )

    plc.connect()

    plc.disconnect()