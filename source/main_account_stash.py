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
from common import common_character
import database as database_base

POE_SESSION_ID = ''
ACCOUNT_NAME = ''

# open up the database
db_connection = database_base.ServerDatabase()
db_connection.db_open()

# load all the base class items into dict (key off base class name)
db_connection.db_base_import_item_class_list()

account_uuid = str(db_connection.db_base_account_upsert(ACCOUNT_NAME))


def com_stash_add_personal_item(stash_json):
    for item_data in stash_json['items']:
        db_connection.db_item_account_upsert(account_uuid, None, item_data)


initial_stash_data = common_character.com_char_get_stash(poe_session_id=POE_SESSION_ID,
                                                         account_name=ACCOUNT_NAME,
                                                         account_league='Standard', tab_ndx=0)
com_stash_add_personal_item(initial_stash_data)
for stash_tab_ndx in range(1, initial_stash_data['numTabs']):
    time.sleep(5)
    com_stash_add_personal_item(
        common_character.com_char_get_stash(poe_session_id=POE_SESSION_ID,
                                            account_name=ACCOUNT_NAME,
                                            account_league='Standard', tab_ndx=stash_tab_ndx))

# close the database
db_connection.db_close()
