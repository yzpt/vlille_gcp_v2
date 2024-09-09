from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import plotly.express as px

def create_layout(locations):       
    
    return html.Div([
        # First column: Parameters
        html.Div([
            html.H2('Parameters'),
        ], className='parameters-div'),
        
        # Second column: Map and information
        html.Div([
            # map div
            html.Div([
                dl.Map([dl.TileLayer()] + [
                    dl.Marker(
                        position=[loc['lat'], loc['lon']],
                        children=[
                            dl.Popup(loc['name'])  # Add a popup with location name
                        ]
                    ) for loc in locations
                ], center=[50.641926, 3.075992], zoom=12, className='map')  # Set initial center and zoom level,
            ], className='map-div'),
            
            # infos div
            html.Div([
                html.H2('Information'),
                html.P('Information content goes here.')
            ], className='info-div'),
        ], className='right-column')
        
    ], fluid=True, className='container')
