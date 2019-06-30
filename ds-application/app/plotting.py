import json
import re
from io import StringIO
from pathlib import Path

import folium
import pandas as pd
import requests
from folium import plugins

save_path = Path(__file__).parent / 'templates' / 'earthquakes.html'

def make_map(qry_params, map_params, save_path=save_path):
    qry_params['format'] = 'csv'
    qry_params['limit'] = 20000  # TODO: flash a warning message
    r = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query', 
                     params=qry_params)
    df = pd.read_csv(StringIO(r.text))

    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [r['longitude'], r['latitude']],
            },
            'properties': {
                'time': r['time'][0:-1],
                'popup': (
                    f"<strong>Time:</strong> {r['time']}<br>"
                    f"<strong>Place:</strong> {r['place']}<br>"
                    f"<strong>Magnitude:</strong> {r['mag']} {r['magType']}<br>"
                    f"<strong>Depth:</strong> {r['depth']}<br>"
                ),
                'icon': 'circle',
                'iconstyle': {
                    'fillOpacity': 0.5,
                    'stroke': 0,
                    'radius': r['mag'] * 2.5
                },
            }
        } for i, r in df.iterrows()
    ]

    m = folium.Map(
        tiles='CartoDBpositron',
        world_copy_jump=True,
        zoom_start=1.5,
        min_zoom=1.5,
        max_zoom=5,
    )

    # add faults
    with open("data/PB2002_boundaries.json", "r") as read_file:
        fault_features = json.load(read_file)
    
    folium.GeoJson(
        {
            'type': 'FeatureCollection',
            'features': fault_features['features'],
        },
        style_function = lambda x: {
            'color': 'red',
            'weight': 0.5,
        }
    ).add_to(m)

    plugins.TimestampedGeoJson(
        {
            'type': 'FeatureCollection',
            'features': features
        },
        period=map_params['period'],
        time_slider_drag_update=True,
        duration=map_params['duration'],
        date_options='YYYY-MM-DD HH UTC'
    ).add_to(m)

    folium.plugins.Fullscreen(
        position='topright',
        force_separate_button=True,
    ).add_to(m)

    m.save(str(save_path))

    return True


def get_quake_feats(qry_params):
    qry_params['format'] = 'csv'
    qry_params['limit'] = 20000  # TODO: flash a warning message
    r = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query', 
                     params=qry_params)
    df = pd.read_csv(StringIO(r.text))

    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [r['longitude'], r['latitude']],
            },
            'properties': {
                'time': r['time'][0:-1],
                'popup': (
                    f"<strong>Time:</strong> {r['time']}<br>"
                    f"<strong>Place:</strong> {r['place']}<br>"
                    f"<strong>Magnitude:</strong> {r['mag']} {r['magType']}<br>"
                    f"<strong>Depth:</strong> {r['depth']}<br>"
                ),
                'icon': 'circle',
                'iconstyle': {
                    'fillOpacity': 0.5,
                    'stroke': 0,
                    'radius': r['mag'] * 2.5
                },
            }
        } for i, r in df.iterrows()
    ]

    return {'type': 'FeatureCollection', 'features': features}
