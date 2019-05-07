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

import uuid


def db_base_account_upsert(self, account_name):
    """
    # upsert into database for the player account names
    """
    self.db_cursor.execute(
        'insert into db_poe_account'
        ' (poe_account_uuid, poe_account_name)'
        ' values (%s,%s)'
        ' on conflict (poe_account_name)'
        ' do update set poe_account_name = %s'
        ' returning poe_account_uuid',
        (str(uuid.uuid4()), account_name, account_name))
    self.db_commit()
    return self.db_cursor.fetchone()[0]


def db_base_account_uuid_by_name(self, account_name):
    self.db_cursor.execute('select poe_account_uuid from db_poe_account'
                           ' where poe_account_name = %s', (account_name,))
    return self.db_cursor.fetchone()[0]


def db_base_account_char_return(self):
    self.db_cursor.execute('select poe_account_uuid, poe_account_name, db_poe_character_uuid, db_poe_character_name'
                           ' from db_poe_account, db_poe_character '
                           'where poe_account_uuid = db_poe_character_account_uuid'
                           ' order by poe_account_name, db_poe_character_name')
    account_char_dict = {}
    for row_data in self.db_cursor.fetchall():
        if row_data['poe_account_uuid'] in account_char_dict:
            temp_list = account_char_dict['poe_account_uuid'][1]
            temp_list.append(row_data['db_poe_character_uuid'], row_data['db_poe_character_name'])
            account_char_dict['poe_account_uuid'] = (row_data['poe_account_name'], temp_list)

        else:
            account_char_dict['poe_account_uuid'] = (row_data['poe_account_name'],
                                                     ((row_data['db_poe_character_uuid'],
                                                      row_data['db_poe_character_name'])))
    return account_char_dict
