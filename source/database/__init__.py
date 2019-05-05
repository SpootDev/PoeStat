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

class ServerDatabase(object):
    """
    Main database class for server
    """
    from database.db_base import db_open, \
        db_close, \
        db_commit, \
        db_rollback, \
        db_table_index_check, \
        db_table_count, \
        db_query, \
        db_parallel_workers
    from database.db_base_account import db_base_account_upsert
    from database.db_base_character import db_base_character_upsert
    from database.db_base_import import db_base_import_item_class_list, \
        db_base_import_item_class_upsert, \
        db_base_import_item_subtype_upsert, \
        db_base_import_character_upsert, \
        db_base_import_monster_upsert, \
        db_base_import_essence_upsert, \
        db_base_import_gem_upsert, \
        db_base_import_mod_upsert, \
        db_base_import_stat_upsert
    from database.db_base_item import db_item_market_class_table, \
        db_item_upsert, \
        db_item_account_upsert, \
        db_item_account_list
    from database.db_base_passive_tree import db_passive_tree_read, \
        db_passive_tree_update
    from database.db_base_stash import db_stash_insert, \
        db_stash_read_all, \
        db_stash_read_all_id, \
        db_stash_all_league, \
        db_stash_delete_null_league
    from database.db_base_status import db_status_read, \
        db_status_update
    from database.db_base_wealth import db_wealth_currency_read, \
        db_wealth_poe_ninja_currency_read, \
        db_wealth_poe_ninja_currency_write
    from database.db_base_users import db_user_list_name_count, \
        db_user_list_name, \
        db_user_detail, \
        db_user_delete, \
        db_user_login
    from database.db_base_version import db_version_check, \
        db_version_update


    # class variables
    sql_conn = None
    sql_cursor = None

    # store the base classes so we don't call every item
    base_item_class_table = {}
