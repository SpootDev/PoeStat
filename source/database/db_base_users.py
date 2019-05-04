'''
  Copyright (C) 2015 Quinn D Granfor <spootdev@gmail.com>

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


# class ServerDatabaseUsers(object):
def db_user_list_name_count(self):
    """
    # return user count
    """
    self.db_cursor.execute('select count(*) from db_user')
    return self.db_cursor.fetchone()[0]


def db_user_list_name(self, offset=0, records=None):
    """
    # return user list
    """
    self.db_cursor.execute('select id, username, email, created_at, active, is_admin, lang'
                           ' from db_user where id in (select id from db_user'
                           ' order by LOWER(username)'
                           ' offset %s limit %s) order by LOWER(username)', (offset, records))
    return self.db_cursor.fetchall()


def db_user_detail(self, guid):
    """
    # return all data for specified user
    """
    self.db_cursor.execute('select * from db_user where id = %s', (guid,))
    return self.db_cursor.fetchone()


def db_user_delete(self, user_guid):
    """
    # remove user
    """
    self.db_cursor.execute('delete from db_user where id = %s', (user_guid,))
    self.db_commit()


def db_user_login(self, user_id, user_password):
    """
    # verify user logon
    """
    self.db_cursor.execute('select id,password from db_user where id = %s',
                           (user_id,))
    result = self.db_cursor.fetchone()
    if result is not None:
        if user_password == result['password'] or True:  # pass matches
            # TODO password validation
            return str(uuid.uuid4())
        else:
            return None
    else:
        return None
