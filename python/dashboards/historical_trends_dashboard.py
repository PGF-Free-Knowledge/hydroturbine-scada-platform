"""
HydroTurbine-SCADA
Historical Trends Dashboard
"""

from flask import Flask

import pandas as pd

import plotly.graph_objects as go

from plotly.subplots import make_subplots


app = Flask(__name__)

HISTORIAN_FILE = "pelton_historical_data.csv"


# ---------------------------------------------------
# READ HISTORIAN
# ---------------------------------------------------

def read_data():

    df = pd.read_csv(HISTORIAN_FILE)

    return df.tail(50)


# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

@app.route("/")

def dashboard():

    df = read_data()

    fig = make_subplots(

        rows=2,
        cols=2,

        subplot_titles=(

            "RPM Trend",
            "FLOW Trend",
            "PRESSURE Trend",
            "POWER Trend"
        )
    )

    # RPM
    fig.add_trace(

        go.Scatter(

            x=df["timestamp"],
            y=df["rpm"],

            mode="lines",

            name="RPM",

            line=dict(width=3)

        ),

        row=1,
        col=1
    )

    # FLOW
    fig.add_trace(

        go.Scatter(

            x=df["timestamp"],
            y=df["flow"],

            mode="lines",

            name="FLOW",

            line=dict(width=3)

        ),

        row=1,
        col=2
    )

    # PRESSURE
    fig.add_trace(

        go.Scatter(

            x=df["timestamp"],
            y=df["pressure"],

            mode="lines",

            name="PRESSURE",

            line=dict(width=3)

        ),

        row=2,
        col=1
    )

    # POWER
    fig.add_trace(

        go.Scatter(

            x=df["timestamp"],
            y=df["power"],

            mode="lines",

            name="POWER",

            line=dict(width=3)

        ),

        row=2,
        col=2
    )

    fig.update_layout(

        template="plotly_dark",

        height=900,

        title="HydroTurbine-SCADA | Historical Industrial Trends"
    )

    graph_html = fig.to_html(full_html=False)

    return f"""

    <html>

    <head>

        <meta http-equiv="refresh" content="5">

    </head>

    <body style="background-color:#020617;">

        {graph_html}

    </body>

    </html>

    """


# ---------------------------------------------------
# RUN SERVER
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)