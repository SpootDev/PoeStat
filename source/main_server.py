'''
  Copyright (C) 2019 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
'''

import os
import subprocess
import sys
import time

from common import common_config_ini
from common import common_docker
from common import common_global
from common import common_hash
from common import common_logging_elasticsearch
from common import common_signal
from common import common_version

# start logging
common_global.es_inst = common_logging_elasticsearch.CommonElasticsearch('main_server')

# set signal exit breaks
common_signal.com_signal_set_break()

common_global.es_inst.com_elastic_index('info', {'PATH': os.environ['PATH']})

# check for and create ssl certs if needed
if not os.path.isfile('./key/cacert.pem'):
    common_global.es_inst.com_elastic_index('info', {'stuff': 'Cert not found, generating.'})
    proc_ssl = subprocess.Popen(['python3', './subprogram_ssl_keygen.py'], shell=False)
    proc_ssl.wait()
    if not os.path.isfile('./key/cacert.pem'):
        common_global.es_inst.com_elastic_index('critical',
                                                {
                                                    'stuff': 'Cannot generate SSL certificate. Exiting.....'})
        sys.exit()

# create crypto keys if needed
if not os.path.isfile('./secure/data.zip'):
    common_global.es_inst.com_elastic_index('info', {'stuff': 'data.zip not found, generating.'})
    data = common_hash.CommonHashCrypto()
    data.com_hash_gen_crypt_key()
    if not os.path.isfile('./secure/data.zip'):
        common_global.es_inst.com_elastic_index('critical',
                                                {
                                                    'stuff': 'Cannot generate crypto. Exiting.....'})
        sys.exit()

# open the database
option_config_json, db_connection = common_config_ini.com_config_read()

# check db version
common_global.es_inst.com_elastic_index('info', {'db1': db_connection.db_version_check()})
common_global.es_inst.com_elastic_index('info', {'db2': common_version.DB_VERSION})
if db_connection.db_version_check() != common_version.DB_VERSION:
    common_global.es_inst.com_elastic_index('info',
                                            {'stuff': 'Database upgrade in progress...'})
    db_create_pid = subprocess.Popen(['python3', './db_update_version.py'], shell=False)
    db_create_pid.wait()
    common_global.es_inst.com_elastic_index('info', {'stuff': 'Database upgrade complete.'})

# setup the docker environment
docker_inst = common_docker.CommonDocker()
# check for swarm id (should already be master then)
docker_info = docker_inst.com_docker_info()
if ('Managers' in docker_info['Swarm'] and docker_info['Swarm']['Managers'] == 0) \
        or 'Managers' not in docker_info['Swarm']:
    common_global.es_inst.com_elastic_index('info',
                                            {'stuff': 'attempting to init swarm as manager'})
    # init host to swarm mode
    docker_inst.com_docker_swarm_init()

# get current working directory from host maps
# this is used so ./data can be used for all the containers launched from docker-py
current_host_working_directory = docker_inst.com_docker_container_bind(container_name='/mkserver',
                                                                       bind_match='/data/devices')

# start up other docker containers if needed
if option_config_json['Docker Instances']['mumble']:
    docker_inst.com_docker_run_mumble(current_host_working_directory)

if option_config_json['Docker Instances']['portainer']:
    docker_inst.com_docker_run_portainer(current_host_working_directory)

if option_config_json['Docker Instances']['teamspeak']:
    docker_inst.com_docker_run_teamspeak(current_host_working_directory)

if option_config_json['Docker Instances']['wireshark']:
    docker_inst.com_docker_run_wireshark()

# sleep for minute so docker doesn't exit
while 1:
    time.sleep(60)

# commit
db_connection.db_commit()

# close the database
db_connection.db_close()
