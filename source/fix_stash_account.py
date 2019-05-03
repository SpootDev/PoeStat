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

import database as database_base

# open up the database
db_connection = database_base.ServerDatabase()
db_connection.db_open()

run_loop = True
while run_loop:
    # this is to build the poe_stash_account_uuid
    for stash_row in db_connection.db_stash_read_all():
        account_uuid = db_connection.db_base_account_upsert(stash_row['account_name'])
        if account_uuid is None:
            run_loop = False
            break
        db_connection.db_query('update db_poe_stashes set poe_stash_account_uuid = \'%s\''
                               ' where poe_stash_uuid = \'%s\'' %
                               (account_uuid, str(stash_row['poe_stash_uuid'])))
        db_connection.db_commit()

# commit all the changes
db_connection.db_commit()
# close the database
db_connection.db_close()
