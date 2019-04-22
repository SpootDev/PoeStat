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


class ServerImport(object):
    """
    Main database class for server data import
    """

    def __init__(self, db_connection):
        self.db_connection = db_connection

    from dataimport.import_base_items import import_base_class_items, \
        import_base_items
    from dataimport.import_base_characters import import_base_character
    from dataimport.import_base_monsters import import_base_monster
    from dataimport.import_base_essences import import_base_essence
    from dataimport.import_base_gems import import_base_gem
    from dataimport.import_base_mods import import_base_mod
    from dataimport.import_base_stats import import_base_stat
    from dataimport.import_base_passive import import_base_passive_tree
