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


def db_status_read(self):
    self.db_cursor.execute('select poe_status_change_id from db_poe_status')
    return self.db_cursor.fetchone()[0]


def db_status_upsert(self, stash_next_id):
    """
    # upsert into database
    """
    self.db_cursor.execute('UPDATE db_poe_status SET poe_status_change_id = %s',
                           (stash_next_id,))
    self.db_commit()
