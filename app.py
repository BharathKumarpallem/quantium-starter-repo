import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px


# ---------- LOAD DATA ----------
df = pd.read_csv("formatted_sales.csv")

# convert date column properly
df["date"] = pd.to_datetime(df["date"])

# ---------- CREATE DASH APP ----------
app = Dash(__name__)

app.layout = html.Div(
    style={"padding": "20px"},

    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={"textAlign": "center"}
        ),

        html.H3(
            "Filter Sales by Region",
            style={"textAlign": "center"}
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"textAlign": "center"}
        ),

        dcc.Graph(id="sales-chart")
    ]
)


# ---------- CALLBACK ----------
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == region]

    # ✅ GROUP SALES BY DATE
    daily_sales = (
        filtered.groupby("date", as_index=False)["Sales"]
        .sum()
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="Sales",
        title="Total Pink Morsel Sales Over Time",
        markers=True
    )

    return fig


# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)