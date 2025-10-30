import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load and prepare data
data = pd.read_csv("data/formatted_output.csv")
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values("date")

# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "backgroundColor": "#f9f9f9",
        "fontFamily": "Arial",
        "padding": "20px"
    },
    children=[
        html.H1(
            "Soul Foods: Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#d63384",
                "marginBottom": "30px"
            }
        ),
        html.Div(
            [
                html.Label("Select a Region:", style={"fontWeight": "bold", "marginRight": "10px"}),
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
                    inputStyle={"marginRight": "5px", "marginLeft": "15px"},
                    style={"textAlign": "center"}
                ),
            ],
            style={"textAlign": "center", "marginBottom": "20px"}
        ),
        dcc.Graph(id="sales-graph")
    ]
)

# Define callback for filtering
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == selected_region]

    fig = px.line(
        filtered_data,
        x="date",
        y="sales",
        color="region",
        title="Pink Morsel Sales Over Time",
        labels={"sales": "Total Sales ($)", "date": "Date"}
    )

    fig.add_shape(
        type="line",
        x0="2021-01-15",
        y0=0,
        x1="2021-01-15",
        y1=1,
        xref="x",
        yref="paper",
        line=dict(color="red", width=2, dash="dash")
    )

    fig.add_annotation(
        x="2021-01-15",
        y=1,
        yref="paper",
        text="Price Increase (Jan 15, 2021)",
        showarrow=False,
        font=dict(color="red"),
        align="right"
    )

    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#f9f9f9"
    )

    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
