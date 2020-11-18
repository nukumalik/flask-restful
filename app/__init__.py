from .config import init_db, init_marshmallow
from .routes import resources
from flask_restful import Api


def create_app(app):
    # Init App
    init_db(app)
    init_marshmallow(app)
    api = Api(app)

    # Routes
    resources(api)
