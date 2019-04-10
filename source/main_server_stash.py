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

import time

import requests

import database as database_base

# TODO rate limit for api
# https://www.pathofexile.com/forum/view-thread/2079853/page/1
STASH_TAB_API_URL = 'http://www.pathofexile.com/api/public-stash-tabs'


def fetch_from_url(stash_last_id=None):
    """
    Download data from specified url
    """
    # requests will auto decompress the gzip
    datafile = requests.get(STASH_TAB_API_URL + '/?id=' + stash_last_id,
                            headers={'accept-encoding': 'gzip'})
    return datafile.json()


# open up the database
db_connection = database_base.ServerDatabase()
db_connection.db_open()
last_stash_id = db_connection.db_status_read()
while True:
    stash_tab_data = fetch_from_url(last_stash_id)
    # verify the ids are not the same (no new stash changes)
    if 'next_change_id' in stash_tab_data:
        if last_stash_id != stash_tab_data['next_change_id']:
            last_stash_id = stash_tab_data['next_change_id']
            for stash_data in stash_tab_data['stashes']:
                # throw out null leagues
                if stash_data['league'] is not None \
                        and stash_data['accountName'] is not None:
                    db_connection.db_stash_insert(stash_data)
            # storing the next id after the stash inserts in case it fails
            db_connection.db_status_update(last_stash_id)
    print(stash_tab_data)
    time.sleep(30)

# close the database
db_connection.db_close()
