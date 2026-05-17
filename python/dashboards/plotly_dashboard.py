"""
HydroTurbine-SCADA
Plotly Industrial Dashboard
"""

import pandas as pd

from flask import Flask

import plotly.graph_objects as go
from plotly.subplots import make_subplots


app = Flask(__name__)

HISTORIAN_FILE = "pelton_historical_data.csv"


# ---------------------------------------------------
# READ HISTORIAN
# ---------------------------------------------------

def read_data():

    df = pd.read_csv(HISTORIAN_FILE)

    return df


# ---------------------------------------------------
# MAIN DASHBOARD
# ---------------------------------------------------

@app.route("/")

def dashboard():

    df = read_data()

    # SHOW ONLY LAST 50 SAMPLES

    df = df.tail(50)

    latest = df.iloc[-1]
 
    fig = make_subplots(

        rows=4,
        cols=2,

        specs=[

            [{"type": "indicator"}, {"type": "indicator"}],

            [{"type": "indicator"}, {"type": "indicator"}],

            [{"type": "xy", "colspan": 2}, None],

            [{"type": "xy", "colspan": 2}, None]

        ],

        vertical_spacing=0.12

    )

    # RPM
    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=latest["rpm"],
            title={"text": "RPM"},
            gauge={
                "axis": {"range": [0, 1200]}
            }
        ),
        row=1,
        col=1
    )

    # FLOW
    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=latest["flow"],
            title={"text": "FLOW"},
            gauge={
                "axis": {"range": [0, 60]}
            }
        ),
        row=1,
        col=2
    )

    # PRESSURE
    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=latest["pressure"],
            title={"text": "PRESSURE"},
            gauge={
                "axis": {"range": [0, 10]}
            }
        ),
        row=2,
        col=1
    )

    # POWER
    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=latest["power"],
            title={"text": "POWER"},
            gauge={
                "axis": {"range": [0, 400]}
            }
        ),
        row=2,
        col=2
    )

# ---------------------------------------------------
# HISTORICAL TRENDS
# ---------------------------------------------------

    timestamps = df["timestamp"]

# RPM TREND

    fig.add_trace(

        go.Scatter(

            x=timestamps,
            y=df["rpm"],

            mode="lines",

            name="RPM Trend"

        ),

        row=3,
        col=1

    )

# POWER TREND

    fig.add_trace(

        go.Scatter(

            x=timestamps,
            y=df["power"],

            mode="lines",

            name="Power Trend"

        ),

        row=4,
        col=1

    )

    fig.update_layout(

        template="plotly_dark",

        height=1200,

        title="HydroTurbine-SCADA | Pelton Industrial Dashboard"

    )

    graph_html = fig.to_html(full_html=False)

    return f"""

    <html>

    <head>

        <meta http-equiv="refresh" content="2">

    </head>

    <body style="background-color:#0f172a;">

        {graph_html}

    </body>

    </html>

    """


# ---------------------------------------------------
# RUN SERVER
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)