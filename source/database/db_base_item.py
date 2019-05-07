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


def db_item_market_class_table(self, table_class):
    # create tables for storing the market data by item class
    self.db_cursor.execute('CREATE TABLE IF NOT EXISTS db_poe_market_%s'
                           ' (market_item_uuid uuid CONSTRAINT market_item_uuid_%s_pk PRIMARY KEY,'
                           ' market_item_stash_uuid uuid REFERENCES db_poe_stashes(poe_stash_uuid)'
                           ' ON DELETE CASCADE, market_item_json jsonb)' %
                           (table_class.lower().replace(' ', '_'),
                            table_class.lower().replace(' ', '_')))
    self.db_cursor.execute('CREATE INDEX IF NOT EXISTS market_item_%s_stash_ndx '
                           'ON db_poe_market_%s (market_item_stash_uuid)' %
                           (table_class.lower().replace(' ', '_'),
                            table_class.lower().replace(' ', '_')))
    self.db_commit()


def db_item_upsert(self, stash_id, item_json):
    """
    # upsert into database
    """
    self.db_cursor.execute('insert into db_poe_market_%s (item_uuid, item_stash_uuid,'
                           ' item_class_id, item_json) values (%s,%s,%s,%s)'
                           ' on conflict (item_uuid) do update set item_json = %s',
                           (item_json['typeLine'].lower().replace(' ', '_'), item_json['id'],
                            stash_id, self.db_cursor.base_item_class_table[
                                item_json['typeLine'].lower().replace(' ', '_')],
                            json.dumps(item_json)))
    self.db_commit()


def db_item_account_upsert(self, account_uuid, item_class, item_json):
    """
    # upsert into database
    """
    self.db_cursor.execute(
        'insert into db_poe_account_items (db_poe_account_item_uuid, db_poe_account_uuid,'
        ' db_poe_account_item_class_uuid, db_poe_account_item_json) values (%s,%s,%s,%s)'
        ' on conflict (db_poe_account_item_uuid) do update set db_poe_account_item_json = %s',
        (item_json['id'], account_uuid, item_class,
         json.dumps(item_json), json.dumps(item_json)))
    self.db_commit()


def db_item_account_list(self, account_uuid):
    self.db_cursor.execute('select db_poe_account_item_json from db_poe_account_items'
                           ' where db_poe_account_item_uuid = %s' % account_uuid)
    return self.db_cursor.fetchall()


def db_item_account_grouped(self, account_uuid, item_subtype=None, offset=0, record_limit=0):
    if item_subtype is None:
        in_sql = 'select item_subtype_uuid from db_poe_item_subtypes'
    else:
        in_sql = 'select item_subtype_uuid from db_poe_item_subtypes'
    self.db_cursor.execute('select db_poe_account_item_json from db_poe_account_items'
                           ' where item_subtype_uuid in (%s)'
                           ' and db_poe_account_item_uuid = %s offset %s limit %s',
                           (in_sql, account_uuid, item_subtype, offset, record_limit))
    return self.db_cursor.fetchall()


def db_item_account_base_subtype(self):
    self.db_cursor.execute('select item_class_uuid, db_poe_item_class_name,'
                           ' item_subtype_uuid, db_poe_item_subtype_name'
                           ' from db_poe_item_class, db_poe_item_subtypes'
                           ' where item_class_uuid = db_poe_item_subtype_class_uuid'
                           ' order by db_poe_item_class_name, db_poe_item_subtype_name')
    return self.db_cursor.fetchall()


def db_item_base_item_tree(self):
    self.db_cursor.execute('select db_poe_item_class.db_poe_item_class_uuid, db_poe_item_class_name,'
                           ' db_poe_item_subtype_uuid, db_poe_item_subtype_name'
                           ' from db_poe_item_class, db_poe_item_subtypes'
                           ' where db_poe_item_class.db_poe_item_class_uuid'
                           ' = db_poe_item_subtypes.db_poe_item_class_uuid'
                           ' order by db_poe_item_class_name, db_poe_item_subtype_name')
    item_dict = {}
    for row_data in self.db_cursor.fetchall():
        if row_data['db_poe_item_class.db_poe_item_class_uuid'] in item_dict:
            temp_list = item_dict[row_data['db_poe_item_class.db_poe_item_class_uuid']][1]
            temp_list.append((row_data['db_poe_item_subtype_uuid'], row_data['db_poe_item_subtype_name']))
            item_dict[row_data['db_poe_item_class.db_poe_item_class_uuid']] = (
            row_data['db_poe_item_class_name'], temp_list)
        else:
            temp_list = []
            temp_list.append((row_data['db_poe_item_subtype_uuid'], row_data['db_poe_item_subtype_name']))
            item_dict[row_data['db_poe_item_class.db_poe_item_class_uuid']] = (
            row_data['db_poe_item_class_name'], temp_list)
    return item_dict
