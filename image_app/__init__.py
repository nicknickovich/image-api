# -*- coding: utf-8 -*-
"""
    image_app
    ~~~~~~~~~

    Module for initializing the app, database, serializer
    and blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

db = SQLAlchemy()
ma = Marshmallow()
api_restful = Api()

def create_app(config_file):
    app = Flask(__name__, instance_relative_config=True)
    with app.app_context():
        app.config.from_pyfile(config_file)

        db.init_app(app)

        from image_app.api.views import api

        app.register_blueprint(api)

        api_restful.init_app(app)

    return app
