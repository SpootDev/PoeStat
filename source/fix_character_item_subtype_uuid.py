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


def do_stuff(sql_query):
    print(sql_query)
    db_connection.db_query(sql_query)


for row_data in db_connection.db_query('select db_poe_account_item_uuid,'
                                       ' db_poe_account_item_json->>\'typeLine\' as subtype_name'
                                       ' from db_poe_account_items'
                                       ' where db_poe_account_item_class_subtype_uuid is NULL'):
    print(row_data)
    subtype_uuid = db_connection.db_item_subtype_uuid_from_name(row_data['subtype_name'])
    if subtype_uuid is not None:
        do_stuff('update db_poe_account_items set db_poe_account_item_class_subtype_uuid = \'%s\''
                 ' where db_poe_account_item_uuid = \'%s\'' %
                 (subtype_uuid, row_data['db_poe_account_item_uuid']))

# commit all the changes
db_connection.db_commit()
# close the database
db_connection.db_close()
