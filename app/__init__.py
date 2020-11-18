from flask_restful import Api

from .config import init_db, init_marshmallow
from .routes import resources


def create_app(app):
    # Init App
    init_db(app)
    init_marshmallow(app)
    api = Api(app)

    # Routes
    resources(api)
