"""
User view in webapp
"""
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g, flash
from flask_login import login_required

blueprint = Blueprint("user", __name__, url_prefix='/users',
                      static_folder="../static")
import sys

sys.path.append('..')
sys.path.append('../..')
from common import common_config_ini
import database as database_base

db_connection = common_config_ini.com_config_read()


def flash_errors(form):
    """
    Display each error on top of form
    """
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@blueprint.route("/")
@login_required
def members():
    """
    Display main members page
    """
    return render_template("users/members.html")


@blueprint.before_request
def before_request():
    """
    Executes before each request
    """
    g.db_connection = database_base.ServerDatabase()
    g.db_connection.db_open()


@blueprint.teardown_request
def teardown_request(exception):  # pylint: disable=W0613
    """
    Executes after each request
    """
    g.db_connection.db_close()
