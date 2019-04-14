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


def db_base_league_upsert(self, league_name, league_json=None):
    """
    # upsert into database for the leagues
    """
    # TODO DO NOTHING doesn't seem to work and return the ID
    if league_json is None:
        self.db_cursor.execute(
            'insert into db_poe_league'
            ' (league_uuid, league_name, league_json)'
            ' values (%s,%s)'
            ' on conflict (league_name)'
            ' do update set league_name = %s'
            ' returning league_uuid',
            (str(uuid.uuid4()), league_name, league_name))
    else:
        self.db_cursor.execute(
            'insert into db_poe_league'
            ' (league_uuid, league_name)'
            ' values (%s,%s,%s)'
            ' on conflict (league_name)'
            ' do update set league_name = %s'
            ' returning league_uuid',
            (str(uuid.uuid4()), league_name, league_json, league_name))
    self.db_commit()
    return self.db_cursor.fetchone()[0]
