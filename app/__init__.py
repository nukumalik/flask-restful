from .config import init_db, init_marshmallow, init_api
from .routes import resources


def create_app(app):
    # Init App
    init_db(app)
    init_marshmallow(app)
    init_api(app)

    # Routes
    resources()
