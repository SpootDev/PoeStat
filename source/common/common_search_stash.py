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
                     veiled_item=False, corrupt_item=False, is_usable=False,
                     fractured_item=False, synthesized_item=False,
                     number_of_sockets=None, number_of_links=None,
                     armor_points=0, es_points=0, evasion_points=0,
                     minimum_ilvl=0,
                     fire_rez=0, cold_rez=0, light_rez=0, chaos_rez=0):
    returned_items = []
    print(shaper_item, eldar_item, veiled_item, corrupt_item, is_usable, fractured_item, synthesized_item,
          number_of_sockets, number_of_links, armor_points, es_points, evasion_points, minimum_ilvl,
          fire_rez, cold_rez, light_rez, chaos_rez)
    for search_item in db_dataset:
        print('item: ', search_item[1])
        print('type: '), type(search_item[1])
        keep_item = True
        if shaper_item:
            if 'shaper' in search_item[1]:
                pass
            else:
                keep_item = False
                continue

        # if eldar_item:
        #     if 'elder' in search_item[1]:
        #         pass
        #     else:
        #         keep_item = False
        #         continue
        #
        # if corrupt_item:
        #     if 'corrupted' in search_item[1]:
        #         pass
        #     else:
        #         keep_item = False
        #         continue
        #
        # if number_of_sockets > 0:
        #     if 'sockets' in search_item[1] and len(search_item[1]['sockets']) >= number_of_sockets:
        #         pass
        #     else:
        #         keep_item = False
        #         continue
        #
        # if armor_points > 0:
        #     if 'properties' in search_item[1] and 'armor' in search_item[1]['properties'] \
        #             and int(search_item[1]['properties']['armor']) >= armor_points:
        #         pass
        #     else:
        #         keep_item = False
        #         continue
        #
        # if es_points > 0:
        #     if 'properties' in search_item[1] and 'energyshield' in search_item[1]['properties'] \
        #             and int(search_item[1]['properties']['energyshield']) >= es_points:
        #         pass
        #     else:
        #         keep_item = False
        #         continue
        #
        # if evasion_points > 0:
        #     if 'properties' in search_item[1] and 'evasion' in search_item[1]['properties'] \
        #             and int(search_item[1]['properties']['evasion']) >= evasion_points:
        #         pass
        #     else:
        #         keep_item = False
        #         continue
        #
        # if minimum_ilvl > 0:
        #     if 'properties' in search_item[1] and 'ilvl' in search_item[1]['properties'] \
        #             and int(search_item[1]['properties']['ilvl']) >= minimum_ilvl:
        #         pass
        #     else:
        #         keep_item = False
        #         continue

        print('keep', keep_item)
        if keep_item:
            returned_items.append(search_item)
    return returned_items
