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

'''
db_poe_market_currency (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
    '''


def db_wealth_currency_read(self):
    self.db_cursor.execute('select market_item_json from db_poe_market_currency')
    for market_record in self.db_cursor.fetchall():
        pass


def db_wealth_poe_ninja_currency_read(self):
    self.db_cursor.execute(
        'select db_poe_currency_json from db_poe_poe_ninja_currency'
        ' order by db_poe_currency_timestamp desc limit 1')
    return self.db_cursor.fetchone()[0]


def db_wealth_poe_ninja_currency_write(self, ninja_json):
    self.db_cursor.execute(
        'insert into db_poe_poe_ninja_currency (db_poe_currency_json) values (%s)',
        (json.dumps(ninja_json),))
    self.db_cursor.commit()
