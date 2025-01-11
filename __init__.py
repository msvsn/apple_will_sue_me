from flask import Flask
from pathlib import Path


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')

    from .routes import main
    app.register_blueprint(main)

    return app