# -*- coding: utf-8 -*-

import json
import sys

sys.path.append('..')
from flask import Blueprint, render_template, g, request, flash

blueprint = Blueprint("admins_messages", __name__, url_prefix='/admin',
                      static_folder="../static")

from common import common_config_ini
from common import common_pagination
import database as database_base

db_connection = common_config_ini.com_config_read()


def flash_errors(form):
    """
    Display errors from list
    """
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@blueprint.route("/messages", methods=["GET", "POST"])
def admin_messages():
    """
    List all messages
    """
    page, per_page, offset = common_pagination.get_page_items()
    pagination = common_pagination.get_pagination(page=page,
                                                  per_page=per_page,
                                                  total=g.db_connection.db_table_count(
                                                      'mm_messages'),
                                                  record_name='messages(s)',
                                                  format_total=True,
                                                  format_number=True,
                                                  )
    return render_template("admin/admin_messages.html",
                           media_dir=g.db_connection.db_message_list(
                               offset, per_page),
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@blueprint.route('/message_delete', methods=["POST"])
def admin_messages_delete_page():
    """
    Delete messages action 'page'
    """
    g.db_connection.db_message_delete(request.form['id'])
    g.db_connection.db_commit()
    return json.dumps({'status': 'OK'})


@blueprint.before_request
def before_request():
    """
    Executes before each request
    """
    g.db_connection = database_base.ServerDatabase()
    g.db_connection.db_open()


@blueprint.teardown_request
def teardown_request(exception):
    """
    Executes after each request
    """
    g.db_connection.db_close()
