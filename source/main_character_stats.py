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
from calculations import calc_character
import database as database_base

POE_SESSION_ID = ''
ACCOUNT_NAME = ''

# open up the database
db_connection = database_base.ServerDatabase()
db_connection.db_open()

# account_uuid = str(db_connection.db_base_account_upsert(ACCOUNT_NAME))

print(calc_character.calculate_character_base_stats('Marauder', 25, character_passive_json=None))


# close the database
db_connection.db_close()
