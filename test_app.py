import pytest
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from dash import Dash
from dash.testing.application_runners import import_app

# This automatically loads your app.py file
@pytest.fixture
def app_runner(dash_duo):
    app = import_app("app")  # app.py should have 'app = Dash(__name__)'
    dash_duo.start_server(app)
    return dash_duo


def test_header_present(app_runner):
    # Check if header text is displayed
    header = app_runner.find_element("h1")
    assert "Soul Foods" in header.text


def test_graph_present(app_runner):
    # Check if the main graph element exists
    graph = app_runner.find_element("div.js-plotly-plot")
    assert graph is not None


def test_region_picker_present(app_runner):
    # Check if the radio items exist
    region_picker = app_runner.find_element("#region-filter")
    assert region_picker is not None
