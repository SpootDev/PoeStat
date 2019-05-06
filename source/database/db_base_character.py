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

import json
import uuid


def db_base_character_upsert(self, account_uuid, character_json, character_passive_json):
    """
    # upsert into database for the player characters from account
    """
    self.db_cursor.execute(
        'insert into db_poe_character'
        ' (db_poe_character_uuid, db_poe_account_uuid, db_poe_character_name,'
        ' db_poe_character_json, db_poe_character_passive_json)'
        ' values (%s,%s,%s,%s,%s)'
        ' on conflict (db_poe_character_name)'
        ' do update set db_poe_character_json = %s, db_poe_character_passive_json = %s'
        ' returning db_poe_character_uuid',
        (str(uuid.uuid4()), account_uuid, character_json['name'], json.dumps(character_json),
         json.dumps(character_passive_json), json.dumps(character_json),
         json.dumps(character_passive_json)))
    self.db_commit()
    return self.db_cursor.fetchone()[0]


def db_base_character_by_account(self, account_uuid):
    """
    return character list by account id
    """
    self.db_cursor.execute(
        'select db_poe_character_uuid, db_poe_character_name, db_poe_character_json'
        ' from db_poe_character'
        ' where db_poe_character_account_uuid = %s'
        ' order by db_poe_character_name', (account_uuid,))
    return self.db_cursor.fetchall()


def db_base_character_by_uuid(self, character_uuid):
    """
    return character data by uuid
    """
    self.db_cursor.execute(
        'select db_poe_character_name, db_poe_character_json'
        ' from db_poe_character'
        ' where db_poe_character_uuid = %s', (character_uuid,))
    return self.db_cursor.fetchone()[0]
