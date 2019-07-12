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

import datetime
import os
import subprocess
import sys
import time

import requests
from common import common_config_ini
from common import common_global
from common import common_hash
from common import common_logging_elasticsearch
from common import common_signal
from common import common_version
from common.common_limiter import *


# https://www.pathofexile.com/forum/view-thread/2079853/page/1
@ratelimited(common_limiter.API_LIMIT['poe_api'][0]
             / common_limiter.API_LIMIT['poe_api'][1])
def poe_api(last_stash_id):
    """
    Rate limiter for PoE api
    """
    common_global.es_inst.com_elastic_index('info', {"here i am in poerate rate":
                                                         datetime.datetime.now().strftime(
                                                             "%H:%M:%S.%f")})
    return requests.get(STASH_TAB_API_URL + '/?id=' + last_stash_id,
                        headers={'accept-encoding': 'gzip'}).json()


STASH_TAB_API_URL = 'http://www.pathofexile.com/api/public-stash-tabs'

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
db_connection = common_config_ini.com_config_read()

# check db version
common_global.es_inst.com_elastic_index('info', {'db1': db_connection.db_version_check()})
common_global.es_inst.com_elastic_index('info', {'db2': common_version.DB_VERSION})
if db_connection.db_version_check() != common_version.DB_VERSION:
    common_global.es_inst.com_elastic_index('info',
                                            {'stuff': 'Database upgrade in progress...'})
    db_create_pid = subprocess.Popen(['python3', './db_update_version.py'], shell=False)
    db_create_pid.wait()
    common_global.es_inst.com_elastic_index('info', {'stuff': 'Database upgrade complete.'})

# pull last id and start populating stash
last_stash_id = db_connection.db_status_read()
# load all the base class items into dict (key off base class name)
db_connection.db_base_import_item_class_list()
while True:
    # requests will auto decompress the gzip
    stash_tab_data = poe_api(last_stash_id)
    # stash_tab_data = requests.get(STASH_TAB_API_URL + '/?id=' + last_stash_id,
    #                               headers={'accept-encoding': 'gzip'}).json()
    # verify the ids are not the same (no new stash changes)
    if 'next_change_id' in stash_tab_data:
        if last_stash_id != stash_tab_data['next_change_id']:
            last_stash_id = stash_tab_data['next_change_id']
            for stash_data in stash_tab_data['stashes']:
                # do not throw out null leagues as this could be a tab delete (readonly tabs)
                if stash_data['accountName'] is not None:
                    db_connection.db_stash_insert(stash_data)
            # storing the next id after the stash inserts in case it fails
            db_connection.db_status_update(last_stash_id)
    time.sleep(5)

# commit
db_connection.db_commit()

# close the database
db_connection.db_close()
