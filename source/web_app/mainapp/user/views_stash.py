"""
User view in webapp
"""
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g, flash, redirect, url_for

blueprint = Blueprint("user_stash", __name__, url_prefix='/users',
                      static_folder="../static")
import sys

sys.path.append('..')
sys.path.append('../..')
from common import common_config_ini
from common import common_pagination
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


@blueprint.route("/stashitemlist/<base_uuid>/<subtype_uuid>")
def stash_item_list(base_uuid, subtype_uuid):
    """
    Display main stash
    """
    try:
        test = g.account_uuid
    except AttributeError:
        return redirect(url_for('user.members'))
    page, per_page, offset = common_pagination.get_page_items()
    pagination = common_pagination.get_pagination(page=page,
                                                  per_page=per_page,
                                                  total=g.db_connection.db_stash_items_by_account_count(g.account_uuid),
                                                  record_name='Stash Items',
                                                  format_total=True,
                                                  format_number=True,
                                                  )
    return render_template('users/user_stash.html',
                           stash_items=g.db_connection.db_stash_items_by_account(g.account_uuid, None, offset, per_page),
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
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
