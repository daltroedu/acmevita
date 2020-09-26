from flask import Flask
from app.config import env_app
from app.extensions.database import db
from app.extensions.migrate import migrate
from app.extensions.schema import ma
from app.extensions.cors import cors


def create_app():
    app = Flask(__name__)
    app.config.from_object(env_app[app.config['ENV']])
    app.url_map.strict_slashes = False

    configure_extensions(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)


def register_blueprints(app):
    from app.blueprints.business.v1 import bp as bp_v1

    app.register_blueprint(bp_v1)