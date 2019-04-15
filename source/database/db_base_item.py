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


def db_item_market_class_table(self, table_class):
    # create tables for storing the market data by item class
    self.db_cursor.db_query('CREATE TABLE IF NOT EXISTS db_poe_market_%s'
                            ' (market_item_uuid uuid, market_item_stash_uuid uuid'
                            ' CONSTRAINT market_item_uuid_pk PRIMARY KEY,'
                            ' market_item_json jsonb)' % table_class.lower().replace(' ', '_'))
    self.db_cursor.db_query('CREATE INDEX IF NOT EXISTS market_item_stash_ndx '
                            'ON db_poe_market_%s (market_item_stash_uuid)' %
                            table_class.lower().replace(' ', '_'))
    self.db_commit()


def db_item_upsert(self, stash_id, item_json):
    """
    # upsert into database
    """
    self.db_cursor.execute('insert into db_poe_item (item_uuid, item_stash_uuid, item_json)'
                           ' values (%s,%s,%s)'
                           ' on conflict (item_uuid)'
                           ' do update set item_json = %s',
                           (str(uuid.uuid4()), stash_id, json.dumps(item_json)))
    self.db_commit()
