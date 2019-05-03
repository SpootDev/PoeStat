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
