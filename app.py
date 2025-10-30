import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed data
data = pd.read_csv("data/formatted_output.csv")

# Ensure date is parsed properly
data["date"] = pd.to_datetime(data["date"])

# Sort by date (just to be safe)
data = data.sort_values("date")

# Create a line chart
fig = px.line(
    data,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time by Region",
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

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Soul Foods: Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
