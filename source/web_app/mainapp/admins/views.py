# -*- coding: utf-8 -*-

import sys

import os

sys.path.append('..')
from flask import Blueprint, render_template, g, request, flash

blueprint = Blueprint("admins", __name__,
                      url_prefix='/admin', static_folder="../static")

from mainapp.admins.forms import AdminSettingsForm

from common import common_config_ini
from common import common_internationalization
from common import common_global
from common import common_hash
from common import common_network
from common import common_string
from common import common_system
from common import common_version
import database as database_base

outside_ip = None
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


@blueprint.route("/")
def admins():
    """
    Display main server page
    """
    global outside_ip
    if outside_ip is None:
        outside_ip = common_network.mk_network_get_outside_ip()
    data_messages = 0
    data_server_info_server_name = 'Spoots PoeStat'
    nic_data = []
    for key, value in common_network.mk_network_ip_addr().items():
        nic_data.append(key + ' ' + value[0][1])
    data_alerts_dismissable = []
    data_alerts = []
    # read in the notifications
    for row_data in g.db_connection.db_notification_read():
        if row_data['mm_notification_dismissable']:  # check for dismissable
            data_alerts_dismissable.append((row_data['mm_notification_guid'],
                                            row_data['mm_notification_text'],
                                            row_data['mm_notification_time']))
        else:
            data_alerts.append((row_data['mm_notification_guid'],
                                row_data['mm_notification_text'], row_data['mm_notification_time']))
    if os.environ['SWARMIP'] != 'None':
        mediakraken_ip = os.environ['SWARMIP']
    else:
        mediakraken_ip = os.environ['HOST_IP']
    return render_template("admin/admins.html",
                           data_user_count=common_internationalization.com_inter_number_format(
                               g.db_connection.db_user_list_name_count()),
                           data_server_info_server_name=data_server_info_server_name,
                           data_host_ip=mediakraken_ip,
                           data_server_info_server_ip=nic_data,
                           data_server_info_server_ip_external=outside_ip,
                           data_server_info_server_version=common_version.APP_VERSION,
                           data_server_uptime=common_system.com_system_uptime(),
                           data_alerts_dismissable=data_alerts_dismissable,
                           data_alerts=data_alerts,
                           data_messages=data_messages,
                           )


@blueprint.route("/admin_sidenav")
def admin_sidenav():
    return render_template("admin/admin_sidenav.html")


@blueprint.route("/messages", methods=["GET", "POST"])
def admin_messages():
    messages = []
    return render_template("admin/admin_messages.html", data_messages=messages)


@blueprint.route("/settings", methods=['GET', 'POST'])
def admin_server_settings():
    """
    Display server settings page
    """
    settings_json = g.db_connection.db_opt_status_read()[0]
    # setup the crypto
    data = common_hash.CommonHashCrypto()
    mediabrainz_api_key = None
    opensubtitles_api_key = None
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        # Docker instances info
        settings_json['Docker Instances']['mumble'] = request.form['docker_mumble']
        settings_json['Docker Instances']['pgadmin'] = request.form['docker_pgadmin']
        settings_json['Docker Instances']['portainer'] = request.form['docker_portainer']
        settings_json['Docker Instances']['teamspeak'] = request.form['docker_teamspeak']
        settings_json['Docker Instances']['wireshark'] = request.form['docker_wireshark']
        # main server info
        settings_json['MediaKrakenServer']['Server Name'] = request.form['servername']
        settings_json['MediaKrakenServer']['MOTD'] = request.form['servermotd']
        # save updated info
        g.db_connection.db_opt_update(settings_json)
    return render_template("admin/admin_server_settings.html",
                           form=AdminSettingsForm(request.form),
                           settings_json=settings_json
                           )


@blueprint.route("/database")
def admin_database_statistics():
    """
    Display database statistics page
    """
    db_stats_count = []
    db_stats_total = 0
    for row_data in g.db_connection.db_pgsql_row_count():
        db_stats_total += row_data[2]
        db_stats_count.append((row_data[1],
                               common_internationalization.com_inter_number_format(row_data[2])))
    db_stats_count.append(
        ('Total records:', common_internationalization.com_inter_number_format(db_stats_total)))
    db_size_data = []
    db_size_total = 0
    for row_data in g.db_connection.db_pgsql_table_sizes():
        db_size_total += row_data['total_size']
        db_size_data.append(
            (row_data['relation'], common_string.com_string_bytes2human(row_data['total_size'])))
    db_size_data.append(('Total Size:', common_string.com_string_bytes2human(db_size_total)))
    return render_template("admin/admin_server_database_stats.html",
                           data_db_size=db_size_data,
                           data_db_count=db_stats_count,
                           data_workers=db_connection.db_parallel_workers())


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
