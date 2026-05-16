"""
HydroTurbine-SCADA
Web Dashboard
"""

import csv

from flask import Flask


app = Flask(__name__)

HISTORIAN_FILE = "pelton_historical_data.csv"


# ---------------------------------------------------
# READ LAST DATA
# ---------------------------------------------------

def get_last_data():

    try:

        with open(HISTORIAN_FILE, mode="r") as file:

            reader = list(csv.DictReader(file))

            if len(reader) == 0:

                return None

            return reader[-1]

    except Exception as e:

        print(e)

        return None


# ---------------------------------------------------
# MAIN DASHBOARD
# ---------------------------------------------------

@app.route("/")

def dashboard():

    data = get_last_data()

    if not data:

        return "<h1>No historian data available</h1>"

    html = f"""

    <html>

    <head>

        <title>HydroTurbine-SCADA</title>

        <meta http-equiv="refresh" content="2">

        <style>

            body {{

                background-color: #0f172a;
                color: white;
                font-family: Arial;
                padding: 40px;

            }}

            h1 {{

                color: #38bdf8;

            }}

            .card {{

                background-color: #1e293b;
                padding: 20px;
                margin: 15px;
                border-radius: 10px;
                width: 300px;

            }}

            .value {{

                font-size: 35px;
                color: #22c55e;

            }}

        </style>

    </head>

    <body>

        <h1>HydroTurbine-SCADA</h1>

        <h2>Pelton Industrial Dashboard</h2>

        <div class="card">

            <h3>RPM</h3>
            <div class="value">{data['rpm']}</div>

        </div>

        <div class="card">

            <h3>FLOW</h3>
            <div class="value">{data['flow']}</div>

        </div>

        <div class="card">

            <h3>PRESSURE</h3>
            <div class="value">{data['pressure']}</div>

        </div>

        <div class="card">

            <h3>POWER</h3>
            <div class="value">{data['power']}</div>

        </div>

        <br>

        <p>Last Update: {data['timestamp']}</p>

        <p>System Status: RUNNING</p>

    </body>

    </html>

    """

    return html


# ---------------------------------------------------
# RUN SERVER
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)