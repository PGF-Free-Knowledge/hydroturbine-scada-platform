# Pelton Mimic Dashboard
# Un mimic es: representación gráfica viva del proceso industrial
"""
HydroTurbine-SCADA
Pelton Mimic Dashboard
"""

from flask import Flask

import pandas as pd


app = Flask(__name__)

HISTORIAN_FILE = "pelton_historical_data.csv"


# ---------------------------------------------------
# READ DATA
# ---------------------------------------------------

def read_data():

    df = pd.read_csv(HISTORIAN_FILE)

    df = df.tail(1)

    return df.iloc[-1]


# ---------------------------------------------------
# API DATA
# ---------------------------------------------------

@app.route("/api/data")

def api_data():

    data = read_data()

    status = "RUNNING"

    if data["flow"] < 30:

        status = "LOW FLOW WARNING"

    return {

        "rpm": round(data["rpm"], 2),
        "flow": round(data["flow"], 2),
        "pressure": round(data["pressure"], 2),
        "power": round(data["power"], 2),
        "status": status
    }

# ---------------------------------------------------
# MAIN DASHBOARD
# ---------------------------------------------------

@app.route("/")

def dashboard():

    data = read_data()

    rpm = round(data["rpm"], 2)
    flow = round(data["flow"], 2)
    pressure = round(data["pressure"], 2)
    power = round(data["power"], 2)

# ---------------------------------------------------
# ALARM LOGIC
# ---------------------------------------------------

    status = "RUNNING"

    status_color = "#22c55e"
    alarm_banner = False


    if pressure > 8:

        status = "HIGH PRESSURE WARNING"

        status_color = "#f59e0b"

        alarm_banner = True


    if rpm > 1100:

        status = "OVER SPEED CRITICAL"

        status_color = "#ef4444"

        alarm_banner = True


    if flow < 30: #if flow < 10:

        status = "LOW FLOW WARNING"

        status_color = "#f59e0b"

        alarm_banner = True

    alarm_html = ""

    if alarm_banner:

        alarm_html = """

        <div class="alarm-banner">

            ⚠ INDUSTRIAL ALARM ACTIVE ⚠

        </div>

        """
    return f"""

    <html>

    <head>

        
        <style>

            body {{

                background-color: #0f172a;
                color: white;
                font-family: Arial;
                margin: 0;
                padding: 0;
            }}

            .header {{

                background-color: #111827;

                padding: 20px;

                text-align: center;

                font-size: 32px;

                font-weight: bold;

                color: #38bdf8;
            }}

            .main-container {{

                display: flex;

                flex-direction: row;

                height: 90vh;
            }}

            .process-area {{

                flex: 3;

                position: relative;

                background-color: #020617;
            }}

            .process-image {{

                width: 100%;

                height: 100%;

                object-fit: contain;
            }}

            .turbine-rotating {{

                position: absolute;

                top: 210px;

                left: 720px;

                width: 130px;

                height: 130px;

                border-radius: 50%;

                animation: turbine-spin 0.5s linear infinite;

                z-index: 10;
            }}

                width: 100%;

                height: 100%;

                object-fit: contain;
            }}

            .panel {{

                flex: 1;

                background-color: #111827;

                padding: 20px;

                border-left: 2px solid #1e293b;
            }}

            .card {{

                background-color: #1e293b;

                padding: 20px;

                margin-bottom: 20px;

                border-radius: 10px;
            }}

            .value {{

                font-size: 40px;

                color: #22c55e;

                margin-top: 10px;
            }}

            .status-running {{

            font-weight: bold;

            font-size: 24px;
            }}

            .water-flow {{

                position: absolute;

                top: 50%;

                left: 10%;

                width: 200px;

                height: 12px;

                background: linear-gradient(
                    90deg,
                    #38bdf8,
                    #0ea5e9,
                    #38bdf8
                );

                border-radius: 10px;

                animation: flow 1s linear infinite;
            }}

            .alarm-banner {{

                background-color: #ef4444;

                color: white;

                text-align: center;

                padding: 15px;

                font-size: 28px;

                font-weight: bold;

                animation: blink 1s infinite;
            }}

            @keyframes turbine-spin {{

                from {{

                    transform: rotate(0deg);
                }}

                to {{

                    transform: rotate(360deg);
                }}
            }}
            @keyframes blink {{

                0% {{
                    opacity: 1;
                }}

                50% {{
                    opacity: 0.3;
                }}

                100% {{
                    opacity: 1;
                }}
            }}
            @keyframes flow {{

                0% {{
                    transform: translateX(0px);
                }}

                50% {{
                    transform: translateX(20px);
                }}

                100% {{
                    transform: translateX(0px);
                }}
            }}

        </style>

    </head>

    <body>
    {alarm_html}

    <div class="header">

            HydroTurbine-SCADA | Pelton Mimic Dashboard

        </div>

        <div class="main-container">

            <div class="process-area">

                <img
                    src="/static/pelton_process.png"
                    class="process-image"
                >

                <div class="water-flow"></div>
                <img
                    src="/static/pelton_runner.png"
                    class="turbine-rotating"
                >

            </div>

            <div class="panel">

                <div class="card">

                    <h2>RPM</h2>

                    <div class="value" id="rpm-value">{rpm}</div>

                </div>

                <div class="card">

                    <h2>FLOW</h2>

                    <div class="value" id="flow-value">{flow}</div>

                </div>

                <div class="card">

                    <h2>PRESSURE</h2>

                    <div class="value" id="pressure-value">{pressure}</div>

                </div>

                <div class="card">

                    <h2>POWER</h2>

                    <div class="value" id="power-value">{power}</div>

                </div>

                <div class="card">

                    <h2>SYSTEM STATUS</h2>

                    <div
                        class="status-running"

                        style="color:{status_color};"
                    >

                        <span id="status-value">{status}</span>

                    </div>

                </div>

            </div>

        </div>

<script>

async function updateData() {{

    const response = await fetch("/api/data");

    const data = await response.json();

    document.getElementById("rpm-value").innerHTML =
        data.rpm;

    document.getElementById("flow-value").innerHTML =
        data.flow;

    document.getElementById("pressure-value").innerHTML =
        data.pressure;

    document.getElementById("status-value").innerHTML =
        data.status;
}}

setInterval(updateData, 2000);

</script>
        

    </body>

    </html>

    """


# ---------------------------------------------------
# RUN SERVER
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)