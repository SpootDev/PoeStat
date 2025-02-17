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


def db_stash_insert(self, share_json):
    """
    # insert share into database
    """
    self.db_cursor.execute('insert into db_poe_stashes (poe_stash_uuid, poe_stash_account_uuid,'
                           ' poe_stash_json_data, poe_stash_id_uuid)'
                           ' values (%s,%s,%s,%s)'
                           ' on conflict (poe_stash_id_uuid)'
                           ' do update set poe_stash_json_data = %s',
                           (str(uuid.uuid4()),
                            self.db_base_account_upsert(share_json['accountName']),
                            json.dumps(share_json), str(share_json['id']),
                            json.dumps(share_json)))
    # TODO - remove the old items?  need to keep track of stuff that's removed, etc
    # insert all the items per stash tab
    for item_json in share_json['items']:
        self.db_cursor.db_item_upsert(str(share_json['id']), item_json)
    self.db_commit()


def db_stash_read_all_id(self):
    self.db_cursor.execute(
        'select poe_stash_json_data->>\'id\' as poe_stash_id from db_poe_stashes')
    return self.db_cursor.fetchall()


def db_stash_read_all(self):
    self.db_cursor.execute(
        'select poe_stash_uuid, poe_stash_json_data->\'accountName\' as account_name'
        ' from db_poe_stashes where poe_stash_account_uuid is NULL limit 2000')
    return self.db_cursor.fetchall()


def db_stash_all_league(self):
    self.db_cursor.execute(
        'select distinct league from (select poe_stash_json_data->\'league\' as league'
        ' from db_poe_stashes) as foo')
    return self.db_cursor.fetchall()


def db_stash_delete_null_league(self):
    self.db_cursor.execute(
        'delete from db_poe_stashes where poe_stash_json_data->>\'league\' is null')
    self.db_commit()


def db_stash_items_by_account_count(self, account_uuid, base_uuid, subtype_uuid, league_uuid=None):
    print(account_uuid, base_uuid, subtype_uuid, league_uuid)
    print(type(account_uuid), type(base_uuid), type(subtype_uuid), type(league_uuid))
    if base_uuid != "0":
        if base_uuid == "-1":
            # all items selected
            self.db_cursor.execute('select count(*) from db_poe_account_items'
                                   ' where db_poe_account_item_account_uuid = %s',
                                   (account_uuid,))
        else:
            # base uuid is set (helmet, gloves, etc)
            self.db_cursor.execute('select count(*) from db_poe_account_items'
                                   ' where db_poe_account_item_account_uuid = %s'
                                   ' and db_poe_account_item_class_subtype_uuid'
                                   ' in (select db_poe_item_subtype_uuid'
                                   ' from db_poe_item_class, db_poe_item_subtypes'
                                   ' where db_poe_item_subtype_class_uuid = db_poe_item_class_uuid'
                                   ' and db_poe_item_class_uuid = %s)',
                                   (account_uuid, base_uuid))
    else:
        # subtype is set (tornado wand, imperial claw, etc)
        self.db_cursor.execute('select count(*) from db_poe_account_items'
                               ' where db_poe_account_item_account_uuid = %s'
                               ' and db_poe_account_item_class_subtype_uuid = %s',
                               (account_uuid, subtype_uuid))
    return self.db_cursor.fetchone()[0]


def db_stash_items_by_account(self, account_uuid, base_uuid, subtype_uuid, league_uuid=None,
                              offset=0, record_limit=0):
    print(account_uuid, base_uuid, subtype_uuid, league_uuid)
    print(type(account_uuid), type(base_uuid), type(subtype_uuid), type(league_uuid))
    if base_uuid != "0":
        if base_uuid == "-1":
            # all items selected
            self.db_cursor.execute('select db_poe_account_item_uuid, db_poe_account_item_json'
                                   ' from db_poe_account_items, db_poe_item_class, db_poe_item_subtypes'
                                   ' where db_poe_account_item_account_uuid = %s'                                  
                                   ' and db_poe_account_item_class_subtype_uuid = db_poe_item_subtype_uuid'
                                   ' and db_poe_item_subtype_class_uuid = db_poe_item_subtype_class_uuid'
                                   ' order by db_poe_item_class_name, db_poe_item_subtype_name'
                                   ' offset %s limit %s',
                                   (account_uuid, offset, record_limit))
        else:
            # base uuid is set (helmet, gloves, etc)
            self.db_cursor.execute('select db_poe_account_item_uuid, db_poe_account_item_json'
                                   ' from db_poe_account_items, db_poe_item_class, db_poe_item_subtypes'
                                   ' where db_poe_account_item_account_uuid = %s'
                                   ' and db_poe_account_item_class_subtype_uuid'
                                   ' in (select db_poe_item_subtype_uuid'
                                   ' from db_poe_item_class, db_poe_item_subtypes'
                                   ' where db_poe_item_subtype_class_uuid = db_poe_item_class_uuid'
                                   ' and db_poe_item_class_uuid = %s)'
                                   ' and db_poe_account_item_class_subtype_uuid = db_poe_item_subtype_uuid'
                                   ' and db_poe_item_subtype_class_uuid = db_poe_item_subtype_class_uuid'
                                   ' order by db_poe_item_class_name, db_poe_item_subtype_name'
                                   ' offset %s limit %s',
                                   (account_uuid, base_uuid, offset, record_limit))
    else:
        # subtype is set (tornado wand, imperial claw, etc)
        self.db_cursor.execute('select db_poe_account_item_uuid, db_poe_account_item_json'
                               ' from db_poe_account_items, db_poe_item_class, db_poe_item_subtypes'
                               ' where db_poe_account_item_account_uuid = %s'
                               ' and db_poe_account_item_class_subtype_uuid = %s'
                               ' and db_poe_account_item_class_subtype_uuid = db_poe_item_subtype_uuid'
                               ' and db_poe_item_subtype_class_uuid = db_poe_item_subtype_class_uuid'
                               ' order by db_poe_item_class_name, db_poe_item_subtype_name'
                               ' offset %s limit %s',
                               (account_uuid, subtype_uuid, offset, record_limit))
    return self.db_cursor.fetchall()


"""
select count(*) from db_poe_stashes where poe_stash_json_data->>'league' is null
 and poe_stash_json_data->>'accountName' is Null
 and JSONB_ARRAY_LENGTH(poe_stash_json_data->'items') = 0
"""
