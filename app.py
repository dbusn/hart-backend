import os

from flask import Flask, render_template
from flask_cors import CORS

from definitions import DISTRIBUTION, RESOURCES
from src.handlers.Dispatcher import Dispatcher
from src.modules.ArduinoConnection import ArduinoConnection
from src.modules.google_api.GoogleApiWrapper import GoogleApiWrapper
from src.helpers.Logger import Logger


if os.environ.keys().__contains__('FLASK_ENV') and os.environ['FLASK_ENV'] == "development" and DISTRIBUTION:
    Logger.log_error("Running in development mode with DISTRIBUTION set to true!")
    raise RuntimeError("Quiting execution!")
elif os.environ.keys().__contains__('FLASK_ENV') and os.environ['FLASK_ENV'] == "production" and not DISTRIBUTION:
    Logger.log_error("Running in production mode with DISTRIBUTION set to false!")
    raise RuntimeError("Quiting execution!")


import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__)
CORS(app)


if os.environ.get("WERKZEUG_RUN_MAIN") or __name__ == "__main__":

    # Initialize dispatcher
    dispatcher = Dispatcher()

    # config singleton ArduinoConnection
    ArduinoConnection().connect_with_config(os.path.join(RESOURCES, 'arduino_config.json'))

    # Check if google api is working correctly
    GoogleApiWrapper(credentials_path=os.path.join(RESOURCES, 'gcloud_credentials.json'))


if DISTRIBUTION:
    @app.route('/', methods=['GET'])
    def standard_route():
        return render_template("index.html")


    @app.errorhandler(404)
    @app.errorhandler(500)
    def error_route(e):
        return render_template("index.html")


if os.environ.get("WERKZEUG_RUN_MAIN") or __name__ == "__main__":
    # Import routes
    from src.routes.Routes import *


if __name__ == "__main__" and DISTRIBUTION:
    log.setLevel(logging.INFO)

    app.run(debug=False, use_reloader=False, threaded=True)