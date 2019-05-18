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

import multiprocessing

import psycopg2
import psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT  # pylint: disable=W0611


def db_open(self):
    """
    # open database and pull in config and create db if not exist
    """
    # setup for unicode
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    # add better uuid mapping
    psycopg2.extras.register_uuid()
    self.sql_conn = psycopg2.connect("dbname='poedb' host='poedb' port=5432 user='postgres'")
    self.sql_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    self.db_cursor = self.sql_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    self.db_cursor.execute('SET TIMEZONE = \'America/Chicago\'')
    self.db_cursor.execute('SET max_parallel_workers_per_gather TO %s;' %
                           multiprocessing.cpu_count())


def db_close(self):
    """
    # close main db file
    """
    self.sql_conn.close()


def db_commit(self):
    """
    # commit changes to media database
    """
    self.sql_conn.commit()


def db_rollback(self):
    """
    # rollback
    """
    self.sql_conn.rollback()


def db_table_index_check(self, resource_name):
    """
    # check for table or index
    """
    self.db_cursor.execute('SELECT to_regclass(\'public.%s\')' % (resource_name,))
    return self.db_cursor.fetchone()[0]


def db_table_count(self, table_name):
    """
    # return count of records in table
    """
    # can't %s due to ' inserted
    # TODO little bobby tables
    self.db_cursor.execute('select count(*) from ' + table_name)
    return self.db_cursor.fetchone()[0]


def db_query(self, query_string):
    """
    # general run anything
    """
    # TODO little bobby tables
    self.db_cursor.execute(query_string)
    try:
        return self.db_cursor.fetchall()
    except:
        return None


def db_parallel_workers(self):
    """
    Return number of workers
    """
    self.db_cursor.execute('show max_parallel_workers_per_gather')
    return self.db_cursor.fetchone()[0]
