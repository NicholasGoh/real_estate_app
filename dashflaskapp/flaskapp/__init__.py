from ddtrace import patch_all
from flask import Flask
from config import Config

patch_all()

def init_flask_app():
    flaskApp = Flask(__name__)
    flaskApp.config.from_object(Config)

    with flaskApp.app_context():
        from . import routes
        # from .plotlydash.dashboard import init_dashboard
        from .plotlydash.dashboard import init_dashboard

        flaskApp = init_dashboard(flaskApp)

    return flaskApp
