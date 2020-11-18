# import os
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

from .config import init_db, init_marshmallow
from .routes import resources


def create_app(app):
    # Init App
    init_db(app)
    init_marshmallow(app)
    api = Api(app)

    # Routes
    resources(api)
    return app
