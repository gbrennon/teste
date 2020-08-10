from flask import Flask
from flask_cors import CORS
from urls import init_resources
from settings import DEBUG, HOST, PORT


def make_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    init_resources(app)

    app.config["DEBUG"] = DEBUG

    CORS(app)

    app.logger.disable = True

    return app


app = make_app()

if __name__ == "__main__":
    app.run(debug=True, port=PORT, host=HOST)

