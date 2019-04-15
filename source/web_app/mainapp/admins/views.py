# -*- coding: utf-8 -*-

import sys

import os

sys.path.append('..')
from flask import Blueprint, render_template, g, request, flash
from flask_login import login_required

blueprint = Blueprint("admins", __name__,
                      url_prefix='/admin', static_folder="../static")
# need the following three items for admin check
import flask
from flask_login import current_user
from functools import wraps
from MediaKraken.admins.forms import AdminSettingsForm

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
option_config_json, db_connection = common_config_ini.com_config_read()


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


def admin_required(fn):
    """
    Admin check
    """

    @wraps(fn)
    @login_required
    def decorated_view(*args, **kwargs):
        common_global.es_inst.com_elastic_index('info', {"admin access attempt by":
                                                             current_user.get_id()})
        if not current_user.is_admin:
            return flask.abort(403)  # access denied
        return fn(*args, **kwargs)

    return decorated_view


@blueprint.route("/")
@login_required
@admin_required
def admins():
    """
    Display main server page
    """
    global outside_ip
    if outside_ip is None:
        outside_ip = common_network.mk_network_get_outside_ip()
    data_messages = 0
    data_server_info_server_name = 'Spoots Media'
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
                           data_active_streams=common_internationalization.com_inter_number_format(
                               0),
                           data_alerts_dismissable=data_alerts_dismissable,
                           data_alerts=data_alerts,
                           data_count_media_files=common_internationalization.com_inter_number_format(
                               g.db_connection.db_known_media_count()),
                           data_count_matched_media=common_internationalization.com_inter_number_format(
                               g.db_connection.db_matched_media_count()),
                           data_count_streamed_media=common_internationalization.com_inter_number_format(
                               0),
                           data_library=common_internationalization.com_inter_number_format(
                               g.db_connection.db_table_count('mm_media_dir')),
                           data_messages=data_messages,
                           data_count_meta_fetch=common_internationalization.com_inter_number_format(
                               g.db_connection.db_table_count('mm_download_que')),
                           )


@blueprint.route("/admin_sidenav")
@login_required
@admin_required
def admin_sidenav():
    return render_template("admin/admin_sidenav.html")


@blueprint.route("/messages", methods=["GET", "POST"])
@login_required
@admin_required
def admin_messages():
    """
    List all NAS devices
    """
    messages = []
    return render_template("admin/admin_messages.html", data_messages=messages)


@blueprint.route("/settings", methods=['GET', 'POST'])
@login_required
@admin_required
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
        if settings_json['API']['musicbrainz'] is not None:
            mediabrainz_api_key = data.com_hash_gen_crypt_decode(
                settings_json['API']['musicbrainz'])
        if settings_json['API']['opensubtitles'] is not None:
            opensubtitles_api_key = data.com_hash_gen_crypt_decode(
                settings_json['API']['opensubtitles'])
    elif request.method == 'POST':
        # api info
        settings_json['API']['musicbrainz'] = data.com_hash_gen_crypt_encode(
            request.form['docker_musicbrainz_code'])
        settings_json['API']['opensubtitles'] = data.com_hash_gen_crypt_encode(
            request.form['metadata_sub_code'])
        # Docker instances info
        settings_json['Docker Instances']['mumble'] = request.form['docker_mumble']
        settings_json['Docker Instances']['pgadmin'] = request.form['docker_pgadmin']
        settings_json['Docker Instances']['portainer'] = request.form['docker_portainer']
        settings_json['Docker Instances']['smtp'] = request.form['docker_smtp']
        settings_json['Docker Instances']['teamspeak'] = request.form['docker_teamspeak']
        settings_json['Docker Instances']['wireshark'] = request.form['docker_wireshark']
        # main server info
        settings_json['MediaKrakenServer']['Server Name'] = request.form['servername']
        settings_json['MediaKrakenServer']['MOTD'] = request.form['servermotd']
        # save updated info
        g.db_connection.db_opt_update(settings_json)
    '''
    activity_purge_interval = SelectField('Purge Activity Data Older Than',
                                          choices=[('Never', 'Never'), ('1 Day', '1 Day'),
                                                   ('Week', 'Week'), ('Month',
                                                                      'Month'),
                                                   ('Quarter', 'Quarter'), ('6 Months',
                                                                            '6 Months'),
                                                   ('Year', 'Year')])
    user_password_lock = SelectField('Lock account after failed attempts',
                                     choices=[('Never', 'Never'), ('3', '3'), ('5', '5'),
                                              ('10', '10')])
    # language = SelectField('Interval', choices=[('Hours', 'Hours'),
    # ('Days', 'Days'), ('Weekly', 'Weekly')])
    # country = SelectField('Interval', choices=[('Hours', 'Hours'),
    # ('Days', 'Days'), ('Weekly', 'Weekly')])
    metadata_with_media = BooleanField('Metadata with Media')
    metadata_sub_down = BooleanField('Download Media Subtitle')
    # meta_language = SelectField('Interval', choices=[('Hours', 'Hours'),\
    # ('Days', 'Days'), ('Weekly', 'Weekly')])
    metadata_sub_skip_if_audio = BooleanField('Skip subtitle if lang in audio track')
    docker_musicbrainz_code = TextField('Brainzcode', validators=[DataRequired(),
                                                                  Length(min=1, max=250)])
    '''
    return render_template("admin/admin_server_settings.html",
                           form=AdminSettingsForm(request.form),
                           settings_json=settings_json,
                           mediabrainz_api_key=mediabrainz_api_key,
                           opensubtitles_api_key=opensubtitles_api_key
                           )


@blueprint.route("/database")
@login_required
@admin_required
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
    g.db_connection = database_base.MKServerDatabase()
    g.db_connection.db_open()


@blueprint.teardown_request
def teardown_request(exception):
    """
    Executes after each request
    """
    g.db_connection.db_close()
