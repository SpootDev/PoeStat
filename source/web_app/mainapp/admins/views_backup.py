# -*- coding: utf-8 -*-

import json
import os
import sys

sys.path.append('..')
from flask import Blueprint, render_template, g, request, flash

blueprint = Blueprint("admins_backup", __name__,
                      url_prefix='/admin', static_folder="../static")

from mainapp.admins.forms import BackupEditForm
from common import common_config_ini
from common import common_file
from common import common_global
from common import common_pagination
from common import common_string
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


@blueprint.route('/backup_delete', methods=["POST"])
def admin_backup_delete_page():
    """
    Delete backup file action 'page'
    """
    file_path, file_type = request.form['id'].split('|')
    if file_type == "Local":
        os.remove(file_path)
    return json.dumps({'status': 'OK'})


@blueprint.route("/backup", methods=["GET", "POST"])
def admin_backup():
    """
    List backups from local fs and cloud
    """
    form = BackupEditForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if request.form['backup'] == 'Update':
                pass
            elif request.form['backup'] == 'Start Backup':
                g.db_connection.db_trigger_insert(('python3',
                                                   './subprogram_postgresql_backup.py'))  # this commits
                flash("Postgresql Database Backup Task Submitted.")
        else:
            flash_errors(form)
    backup_enabled = False
    backup_files = []
    local_file_backups = common_file.com_file_dir_list('/poestat/backup',
                                                       'dump', False, False, True)
    if local_file_backups is not None:
        for backup_local in local_file_backups:
            backup_files.append((backup_local[0], 'Local',
                                 common_string.com_string_bytes2human(backup_local[1])))

    page, per_page, offset = common_pagination.get_page_items()
    pagination = common_pagination.get_pagination(page=page,
                                                  per_page=per_page,
                                                  total=len(backup_files),
                                                  record_name='backups',
                                                  format_total=True,
                                                  format_number=True,
                                                  )
    return render_template("admin/admin_backup.html", form=form,
                           backup_list=sorted(backup_files, reverse=True),
                           data_interval=('Hours', 'Days', 'Weekly'),
                           data_enabled=backup_enabled,
                           page=page,
                           per_page=per_page,
                           pagination=pagination
                           )


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
