# Qué hace este archivo
# DB Siemens
# offsets
# tipos de variables
# tags industriales
# nomenclatura SCADA
# integración futura

"""
HydroTurbine-SCADA
PLC Tag Definitions
"""

# ---------------------------------------------------
# PELTON TAGS
# ---------------------------------------------------

PELTON_TAGS = {

    "rpm": {
        "db": 1,
        "start": 0,
        "type": "REAL"
    },

    "flow": {
        "db": 1,
        "start": 4,
        "type": "REAL"
    },

    "pressure": {
        "db": 1,
        "start": 8,
        "type": "REAL"
    },

    "power": {
        "db": 1,
        "start": 12,
        "type": "REAL"
    }

}

# ---------------------------------------------------
# FRANCIS TAGS
# ---------------------------------------------------

FRANCIS_TAGS = {

    "rpm": {
        "db": 2,
        "start": 0,
        "type": "REAL"
    },

    "torque": {
        "db": 2,
        "start": 4,
        "type": "REAL"
    },

    "brake_pressure": {
        "db": 2,
        "start": 8,
        "type": "REAL"
    },

    "shaft_speed": {
        "db": 2,
        "start": 12,
        "type": "REAL"
    }

}

# ---------------------------------------------------
# SYSTEM TAGS
# ---------------------------------------------------

SYSTEM_TAGS = {

    "alarm_general": {
        "db": 10,
        "start": 0,
        "type": "BOOL"
    },

    "system_running": {
        "db": 10,
        "start": 1,
        "type": "BOOL"
    }

}


# ---------------------------------------------------
# TEST
# ---------------------------------------------------

if __name__ == "__main__":

    print("===================================")
    print("HydroTurbine-SCADA")
    print("PLC Tag Definitions")
    print("===================================")

    print("\nPelton Tags:")

    for tag, data in PELTON_TAGS.items():

        print(f"{tag} -> {data}")

    print("\nFrancis Tags:")

    for tag, data in FRANCIS_TAGS.items():

        print(f"{tag} -> {data}")

    print("\nSystem Tags:")

    for tag, data in SYSTEM_TAGS.items():

        print(f"{tag} -> {data}")