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
