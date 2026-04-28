markdown
# Optimized Public Transport Accessibility Analysis

This project provides a web-based tool for analyzing public transportation accessibility in Abu Dhabi. The tool integrates static datasets and real-time data to offer actionable insights and interactive visualizations.

## Features

1. **Real-time Data Integration**: Combines static datasets with real-time updates from GPS tracking and user feedback.
2. **Interactive Mapping**: Visualize bus routes, metro lines, and accessibility features on an interactive map.
3. **Custom Filters**: Filter transportation data by type, frequency, and operational hours.
4. **Accessibility Insights**: Analyze features like wheelchair accessibility and other facilities for people with special needs.
5. **Feedback Mechanism**: Users can report issues like delays or missing features, which will be used to update the dataset.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- Pandas
- Geopandas
- Folium

### Installation

1. Clone the repository:
   bash
   git clone https://github.com/username/abu-dhabi-transport-accessibility.git
   cd abu-dhabi-transport-accessibility
   
2. Install dependencies:
   bash
   pip install -r requirements.txt
   
3. Place the dataset files (`Public_Transport_Accessibility_AbuDhabi.csv` and `Public_Transport_Stops_and_Routes_AbuDhabi.geojson`) in the project directory.

### Usage

1. Run the Flask app:
   bash
   python app.py
   
2. Access the API at `http://127.0.0.1:5000/api/routes`.
3. Access the interactive map at `http://127.0.0.1:5000/map`.

### API Endpoints

#### GET /api/routes

Filters and returns transportation routes based on query parameters.

**Query Parameters:**
- `type` (optional): Type of transportation (e.g., bus, metro).
- `frequency` (optional): Minimum frequency of service.

**Example Request:**
http
GET /api/routes?type=bus&frequency=15


**Example Response:**

[
  {
    "route_number": "E100",
    "transport_type": "bus",
    "frequency": 15,
    "stop_locations": "[24.4539, 54.3773]",
    "accessibility_features": "Wheelchair Accessible"
  },
  ...
]


#### GET /map

Displays an interactive map showing public transportation routes and stops.

### Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the Open Data License.
