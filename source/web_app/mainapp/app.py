# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import os
from mainapp import public, user, admins
from mainapp.assets import assets
from mainapp.extensions import (
    bcrypt,
    db,
)
from mainapp.settings import ProdConfig
from flask import Flask, render_template
from flask_uwsgi_websocket import GeventWebSocket


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    websocket = GeventWebSocket(app)
    return app


def register_extensions(app):
    assets.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    return None


def register_blueprints(app):
    # load up public bps
    app.register_blueprint(public.views.blueprint)
    # load up user bps
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(user.views_character.blueprint)
    app.register_blueprint(user.views_search.blueprint)
    # load up admin bps
    app.register_blueprint(admins.views.blueprint)
    app.register_blueprint(admins.views_backup.blueprint)
    app.register_blueprint(admins.views_cron.blueprint)
    app.register_blueprint(admins.views_docker.blueprint)
    return None


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code

    for errcode in [401, 403, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
