import os
import atexit

from flask import Flask, render_template
from flask_cors import CORS

from definitions import DISTRIBUTION, RESOURCES, CONFIG_FILE_NAME
from src.handlers.Dispatcher import Dispatcher
from src.modules.PrototypeConnection import PrototypeConnection
from src.modules.google_api.GoogleApiWrapper import GoogleApiWrapper
from src.routes.Routes import init_views
import logging


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def close_prototype_connection():
    PrototypeConnection().close_connection()


atexit.register(close_prototype_connection)


def initialize(application):
    # Initialize dispatcher
    dispatcher = Dispatcher()

    # config singleton PrototypeConnection
    PrototypeConnection().connect_with_config(os.path.join(RESOURCES, "sleeve_config_files", CONFIG_FILE_NAME))

    # Check if google api is working correctly
    GoogleApiWrapper(credentials_path=os.path.join(RESOURCES, 'gcloud_credentials.json'))

    # Initialize routes
    init_views(application, dispatcher)

    # If running in distribution mode, then set standard routes and launch browser
    if DISTRIBUTION:
        @app.route('/', methods=['GET'])
        def standard_route():
            return render_template("index.html")

        @app.errorhandler(404)
        @app.errorhandler(500)
        def error_route(e):
            return render_template("index.html")

        log.setLevel(logging.INFO)
        import webbrowser
        webbrowser.open("http://localhost:5000")


# Initialize flask app
app = Flask(__name__)

# Initialize CORS
CORS(app)

# Initialize rest of the backend
initialize(app)

