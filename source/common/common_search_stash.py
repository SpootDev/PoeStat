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


# account_uuid and league_uuid not needed as the db query did that
def com_search_stash(db_dataset, shaper_item=False, eldar_item=False,
                     veiled_item=False, corrupted_item=False, beastcraft_item=False,
                     fractured_item=False, synthesized_item=False,
                     number_of_sockets=None, number_of_links=None,
                     armor_points=0, es_points=0, evasion_points=0, chance_to_block=0,
                     life_points=0, mana_points=0, minimum_ilvl=0,
                     fire_rez=0, cold_rez=0, light_rez=0, chaos_rez=0):
    returned_items = []
    print('search')
    for search_item in db_dataset:
        print('item: ', search_item)
        keep_item = True
        if shaper_item:
            if 'shaper' in search_item[1] and search_item[1]['shaper']:
                pass
            else:
                keep_item = False
                continue

        if eldar_item:
            if 'elder' in search_item[1] and search_item[1]['elder']:
                pass
            else:
                keep_item = False
                continue

        if number_of_sockets > 0:
            if 'sockets' in search_item[1] and len(search_item[1]['sockets']) >= number_of_sockets:
                pass
            else:
                keep_item = False
                continue

        if armor_points > 0:
            if 'properties' in search_item[1] and 'armor' in search_item[1]['properties'] \
                    and int(search_item[1]['properties']['armor']) >= armor_points:
                pass
            else:
                keep_item = False
                continue

        if keep_item:
            returned_items.append(search_item)
    return returned_items
