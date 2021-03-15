from ddtrace import patch_all
from flask import Flask
from config import Config
from flask_googlemaps import GoogleMaps

patch_all()

# starts flask app then dash app within flask that controls plotly
def init_flask_app():
    flaskApp = Flask(__name__)
    flaskApp.config.from_object(Config)
    GoogleMaps(flaskApp, key='AIzaSyAPzHStilkPLPMqHJI0njg4RDkKV8vAPX0')

    with flaskApp.app_context():
        from . import routes
        from .macros_plotly.dashboard import init_dashboard

        flaskApp = init_dashboard(flaskApp)
    return flaskApp
