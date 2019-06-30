import datetime
import json
import re

import dateutil.parser
import pandas as pd
from flask import Flask, redirect, render_template, request, url_for

from .config import Config
from .plotting import make_map, get_quake_feats


def create_app():
    """Create and configure instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/gold')
    def gold():
        return render_template('gold.html')

    @app.route('/sp500')
    def sp500():
        return render_template('sp500.html')

    @app.route('/intermarket')
    def intermarket():
        return render_template('intermarket.html')

    @app.route('/marketmodels')
    def marketmodels():
        return render_template('marketmodels.html')

    # Danielle
    @app.route('/damage')
    def damage():
        return render_template('damage.html')

    @app.route('/tsunami')
    def tsunami():
        return render_template('tsunami.html')

    @app.route('/damagecost')
    def damagecost():
        return render_template('damagecost.html')

    # Shilpa
    @app.route('/us_events')
    def us_events():
        return render_template('us_events.html')

    @app.route('/predictions')
    def predictions():
        return render_template('predictions.html')

    @app.route('/activityanalysis')
    def activityanalysis():
        return render_template('activityanalysis.html')

    # Temp fix for iframe
    @app.route('/tempearthquakes')
    def tempearthquakes():
        return render_template('temp_earthquakes.html')


    @app.route('/map', methods=['GET', 'POST'])
    def map():
        dt_end = datetime.datetime.utcnow()
        dt_beg = (dt_end - datetime.timedelta(days=30)).isoformat()
        dt_end = dt_end.isoformat()
        qry_params = {}
        try:
            qry_params['starttime'] = parse_dtstr(
                request.values.get('starttime', dt_beg))
            qry_params['endtime'] = parse_dtstr(
                request.values.get('endtime', dt_end))
        except ValueError:
            qry_params['starttime'] = parse_dtstr(dt_beg)
            qry_params['endtime'] = parse_dtstr(dt_end)
            pass  # TODO: flash message "Invalid Date, reverted to defaults"
        
        qry_params['minmagnitude'] = request.values.get('minmagnitude', '2.5')
        
        map_params = {}
        map_params['period_amt'] = request.values.get('period_amt', '6')
        map_params['period_unit'] = request.values.get('period_unit', 'Hours')
        
        t_prefix = 'T' if map_params['period_unit'] == 'Hours' else ''
        
        map_params['period'] = ('P' + t_prefix + map_params['period_amt'] + 
                                map_params['period_unit'][0])

        duration = int(map_params['period_amt']) * 2
        map_params['duration'] = re.sub(r'\d+', str(duration), 
                                        map_params['period'])

        # get quake geojson
        quake_feats = get_quake_feats(qry_params)

        # add faults
        with open("data/PB2002_boundaries.json", "r") as read_file:
            fault_feats = json.load(read_file)
        
        fault_feats = {
            'type': 'FeatureCollection',
            'features': fault_feats['features'],
        }

        return render_template('map.html', qry_params=qry_params, 
                               map_params=map_params, fault_feats=fault_feats,
                               quake_feats=quake_feats)

    @app.route('/html_plot/<string:html_name>')
    def html_plot(html_name):
        return render_template(f"/html_plot/{html_name}")
    
    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html")

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("500.html")

    return app


def parse_dtstr(dtstr):
    return dateutil.parser.parse(dtstr).strftime("%Y-%m-%d %H:%M")
