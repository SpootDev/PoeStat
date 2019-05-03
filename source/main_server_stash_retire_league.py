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

'''
This will be run at end of league. Will remove all records from the ending league
and store them in an archive table.
'''

import sys
import database as database_base

# open up the database
db_connection = database_base.ServerDatabase()
db_connection.db_open()

# check that league is passed
if sys.argv[1]:
    # TODO does the stash id simply pop into standard via league name change?
    db_connection.db_query('CREATE TABLE db_poe_stashes_%s AS '
                           'SELECT * FROM db_poe_stashes'
                           ' WHERE poe_stash_json_data->>\'league\' ? %s'
                           % (sys.argv[1], sys.argv[1]))
    db_connection.db_query('delete from db_poe_stashes'
                           ' where poe_stash_json_data->>\'league\' ? %s',
                           (sys.argv[1],))
else:
    print('Must enter league to retire!')

# close the database
db_connection.db_close()
