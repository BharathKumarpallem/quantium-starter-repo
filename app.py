import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# read processed data
df = pd.read_csv("formatted_sales.csv")

# convert date column
df["date"] = pd.to_datetime(df["date"])

# sort by date
df = df.sort_values("date")

# create line chart
fig = px.line(
    df,
    x="date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

# create dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis Dashboard"),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)