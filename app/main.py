from dash import dash
import dash_bootstrap_components as dbc
import json
import requests

import config
from layout import create_layout

print('------------------------------------')
print('Starting Dash app...')
# Fetch data from API
# print(f"Fetching data from {config.Config.API_URL}")
# response = requests.get(config.Config.API_URL)
# print(f"Response status code: {response.status_code}")
# data = response.text
# data = json.loads(data)
print("Fetching data from data.json")
with open('data.json') as f:
    data = json.load(f)
features = data['features']

# Extract coordinates and properties
locations = [{'lat': feature['geometry']['coordinates'][1],
              'lon': feature['geometry']['coordinates'][0],
              'name': feature['properties'].get('name', 'No Name')}  # Adjust property names as needed
             for feature in features]

print(f"Extracted {len(locations)} locations")

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
print("Dash app created")

app.layout = create_layout(locations)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
