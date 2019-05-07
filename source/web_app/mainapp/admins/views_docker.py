# -*- coding: utf-8 -*-

import sys

sys.path.append('..')
from flask import Blueprint, render_template, g, flash

blueprint = Blueprint("admins_docker", __name__,
                      url_prefix='/admin', static_folder="../static")

from common import common_config_ini
from common import common_docker
from common import common_global
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


@blueprint.route("/docker_stat")
def docker_stat():
    """
    Docker statistics including swarm
    """
    docker_inst = common_docker.CommonDocker()
    # it returns a dict, not a json
    docker_info = docker_inst.com_docker_info()
    common_global.es_inst.com_elastic_index('info', {'Docker info': docker_info})
    if 'Managers' not in docker_info['Swarm'] or docker_info['Swarm']['Managers'] == 0:
        docker_swarm = "Cluster not active"
    else:
        docker_swarm = docker_inst.com_docker_swarm_inspect()[
            'JoinTokens']['Worker']
    return render_template("admin/admin_docker.html",
                           data_host=docker_info,
                           data_swam=docker_swarm
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
