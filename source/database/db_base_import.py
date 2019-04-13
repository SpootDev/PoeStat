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


def db_base_import_item_class_upsert(self, base_class, item_json):
    """
    # upsert into database for the "class"
    """
    self.db_cursor.execute(
        'insert into db_poe_item_class'
        ' (item_class_uuid, db_poe_item_class_name, db_poe_item_class_json)'
        ' values (%s,%s,%s)'
        ' on conflict (db_poe_item_class_name)'
        ' do update set db_poe_item_class_json = %s returning item_class_uuid',
        (str(uuid.uuid4()), base_class, json.dumps(item_json), json.dumps(item_json)))
    self.db_commit()
    return self.db_cursor.fetchone()[0]


def db_base_import_item_subtype_upsert(self, item_json, class_uuid):
    """
    Upsert into database for the subclass of the class items
    """
    self.db_cursor.execute(
        'insert into db_poe_item_subtypes'
        ' (item_subtype_uuid, db_poe_item_subtype_name, db_poe_item_subtype_json,'
        ' db_poe_item_subtype_class_uuid)'
        ' values (%s,%s,%s,%s)'
        ' on conflict (db_poe_item_subtype_name)'
        ' do update set db_poe_item_subtype_json = %s,'
        ' db_poe_item_subtype_class_uuid = %s',
        (str(uuid.uuid4()), item_json['name'], json.dumps(item_json),
         class_uuid, json.dumps(item_json), class_uuid))
    self.db_commit()


def db_base_import_character_upsert(self, character_json):
    """
    Upsert into database for the character classes
    """
    self.db_cursor.execute(
        'insert into db_poe_character '
        ' (db_poe_character_uuid, db_poe_character_name, db_poe_character_json)'
        ' values (%s,%s,%s)'
        ' on conflict (db_poe_character_name)'
        ' do update set db_poe_character_json = %s',
        (str(uuid.uuid4()), character_json['name'], json.dumps(character_json), json.dumps(character_json)))
    self.db_commit()



def db_base_import_monster_upsert(self, monster_level, monster_json):
    """
    Upsert into database for the base monster stats
    """
    self.db_cursor.execute(
        'insert into db_poe_monster_base '
        ' (db_poe_monster_uuid, db_poe_monster_level , db_poe_monster_json)'
        ' values (%s,%s,%s)'
        ' on conflict (db_poe_monster_level)'
        ' do update set db_poe_monster_json = %s',
        (str(uuid.uuid4()), monster_level, json.dumps(monster_json), json.dumps(monster_json)))
    self.db_commit()


def db_base_import_essence_upsert(self, essence_json):
    """
    Upsert into database for the base essence
    """
    self.db_cursor.execute(
        'insert into db_poe_essence_base'
        ' (db_poe_essence_uuid, db_poe_essance_name, db_poe_essence_json)'
        ' values (%s,%s,%s)'
        ' on conflict (db_poe_essance_name)'
        ' do update set db_poe_essence_json = %s',
        (str(uuid.uuid4()), essence_json['name'], json.dumps(essence_json), json.dumps(essence_json)))
    self.db_commit()


def db_base_import_gem_upsert(self, base_gem, gem_json):
    """
    Upsert into database for the base gems
    """
    self.db_cursor.execute(
        'insert into db_poe_gem_base'
        ' (db_poe_gem_uuid, db_poe_gem_name, db_poe_gem_json)'
        ' values (%s,%s,%s)'
        ' on conflict (db_poe_gem_name)'
        ' do update set db_poe_gem_json = %s',
        (str(uuid.uuid4()), base_gem, json.dumps(gem_json), json.dumps(gem_json)))
    self.db_commit()
