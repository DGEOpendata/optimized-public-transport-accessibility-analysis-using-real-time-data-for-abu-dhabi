python
import pandas as pd
import geopandas as gpd
import folium
from flask import Flask, request, jsonify

# Load the datasets
transport_data = pd.read_csv('Public_Transport_Accessibility_AbuDhabi.csv')
geo_data = gpd.read_file('Public_Transport_Stops_and_Routes_AbuDhabi.geojson')

# Initialize Flask app
app = Flask(__name__)

# Function to filter data based on user input
def filter_routes(transport_data, route_type=None, frequency=None):
    filtered_data = transport_data
    if route_type:
        filtered_data = filtered_data[filtered_data['transport_type'] == route_type]
    if frequency:
        filtered_data = filtered_data[filtered_data['frequency'] >= frequency]
    return filtered_data

@app.route('/api/routes', methods=['GET'])
def get_routes():
    route_type = request.args.get('type')
    frequency = request.args.get('frequency', type=int)
    filtered_data = filter_routes(transport_data, route_type, frequency)
    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/map', methods=['GET'])
def map_view():
    m = folium.Map(location=[24.4539, 54.3773], zoom_start=12)
    for _, row in geo_data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['stop_name']
        ).add_to(m)
    return m._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)
