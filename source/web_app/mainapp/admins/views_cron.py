# -*- coding: utf-8 -*-

import json
import sys

sys.path.append('..')
from flask import Blueprint, render_template, g, request, flash

blueprint = Blueprint("admins_cron", __name__,
                      url_prefix='/admin', static_folder="../static")

from mainapp.admins.forms import CronEditForm

from common import common_config_ini
from common import common_global
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


@blueprint.route('/cron')
def admin_cron_display_all():
    """
    Display cron jobs
    """
    page, per_page, offset = common_pagination.get_page_items()
    pagination = common_pagination.get_pagination(page=page,
                                                  per_page=per_page,
                                                  total=g.db_connection.db_cron_list_count(False),
                                                  record_name='Cron Jobs',
                                                  format_total=True,
                                                  format_number=True,
                                                  )
    return render_template('admin/admin_cron.html',
                           media_cron=g.db_connection.db_cron_list(
                               False, offset, per_page),
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@blueprint.route('/cron_run/<guid>', methods=['GET', 'POST'])
def admin_cron_run(guid):
    """
    Run cron jobs
    """
    common_global.es_inst.com_elastic_index('info', {'admin cron run': guid})
    cron_job_data = g.db_connection.db_cron_info(guid)
    route_key = 'mkque'
    exchange_key = 'mkque_ex'
    message_type = None
    message_subtype = None
    # no need to do the check since default
    # TODO what the heck do I mean with 'since default'?
    # if cron_file_path == './subprogram_postgresql_backup.py'\
    #     or cron_file_path == './subprogram_create_chapter_images.py':
    #     elif cron_file_path == './subprogram_postgresql_vacuum.py':
    #     elif cron_file_path == './subprogram_file_scan.py':
    #     elif cron_file_path == './subprogram_roku_thumbnail_generate.py':
    #     elif cron_file_path == './subprogram_sync.py':
    #     pass

    # TODO these should feed into metadata program
    # if cron_job_data['mm_cron_file_path'] == './subprogram_update_create_collections.py' \
    #         or cron_job_data['mm_cron_file_path'] == './subprogram_tmdb_updates.py':
    #     route_key = 'themoviedb'
    #     exchange_key = 'mkque_metadata_ex'
    #
    # if cron_job_data['mm_cron_file_path'] == './subprogram_schedules_direct_updates.py':
    #     route_key = 'mkque_metadata'
    #     exchange_key = 'mkque_metadata_ex'

    return render_template('admin/admin_cron.html')


@blueprint.route('/cron_edit/<guid>', methods=['GET', 'POST'])
def admin_cron_edit(guid):
    """
    Edit cron job page
    """
    form = CronEditForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            # request.form['name']
            # request.form['description']
            # request.form['enabled']
            # request.form['interval']
            # request.form['time']
            # request.form['script_path']
            # request.form['json']
            # common_global.es_inst.com_elastic_index('info', {'stuff':'cron edit info: %s %s %s', (addr, share, path))
            pass
    return render_template('admin/admin_cron_edit.html', guid=guid, form=form)


@blueprint.route('/cron_delete', methods=["POST"])
def admin_cron_delete_page():
    """
    Delete action 'page'
    """
    g.db_connection.db_cron_delete(request.form['id'])
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
