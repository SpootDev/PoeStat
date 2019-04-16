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


def import_base_class_items(self):
    class_uuid_table = {}
    with open('./poedata/data/item_classes.json') as file_pointer:
        item_data = json.load(file_pointer)
        for base_class in item_data:
            # create table for base type
            self.db_connection.db_item_market_class_table(base_class)
            # insert into class table
            class_uuid_table[base_class] = self.db_connection.db_base_import_item_class_upsert(
                base_class, item_data[base_class])
    return class_uuid_table


def import_base_items(self, class_uuid_array):
    with open('./poedata/data/base_items.json') as file_pointer:
        item_data = json.load(file_pointer)
        for base_subtype in item_data:
            self.db_connection.db_base_import_item_subtype_upsert(
                item_data[base_subtype],
                class_uuid_array[item_data[base_subtype]['item_class']])
