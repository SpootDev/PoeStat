"""
User view in webapp
"""
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g, flash

blueprint = Blueprint("user_character", __name__, url_prefix='/users',
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


@blueprint.route("/charlist/<account_uuid>")
def character_list(account_uuid):
    """
    Display main members page
    """
    g.account_uuid = account_uuid
    return render_template("users/user_character_list.html",
                           character_list=g.db_connection.db_base_character_by_account(account_uuid),
                           account_player=g.db_connection.db_base_account_char_return(),
                           data_items=g.db_connection.db_item_base_item_tree()
                           )


@blueprint.route("/chardetail/<characteruuid>")
def character_detail(characteruuid):
    """
    Display character detail
    """
    return render_template("users/user_character_detail.html",
                           character_detail=g.db_connection.db_base_character_by_uuid(characteruuid),
                           account_player=g.db_connection.db_base_account_char_return(),
                           data_items=g.db_connection.db_item_base_item_tree()
                           )


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
