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

'''

Every 10 strength grants
    an additional 5 maximum life.
    2% increased melee physical damage.

Every 10 Dexterity grants
    An additional 20 accuracy rating
    2% increased evasion rating
    
Every 10 Intelligence grants
    An additional 5 maximum mana
    2% increased maximum energy shield
'''

character_level_bonus = {'Life': 12,
                         'Mana': 6,
                         'Evasion rating': 3,
                         'Main hand accuracy rating': 2}

character_class_base = {'Marauder': {'STR': 32, 'DEX': 14, 'INT': 14,
                                     'Life': 66,
                                     'Mana': 47,
                                     'Damage per second': 5,
                                     'Chance to hit %': 83,
                                     'Attacks per second': 1.2,
                                     'Main hand total combined damage': '2-8',
                                     'Main hand physical damage': '2-8',
                                     'Main hand accuracy rating': 28,
                                     'Main hand critical strike damage multiplier %': 150,
                                     'Endurance charge': '0/3',
                                     'Physical damage reduction per endurance charge %': 4,
                                     'Additional elemental reduction per endurance charge %': 4,
                                     'Frenzy charges': '0/3',
                                     'Attack speed increase per frenzy charge %': 4,
                                     'Cast speed increase per frenzy charge %': 4,
                                     'Damage modifier per frenzy charge %': 4,
                                     'Power charges': '0/3',
                                     'Critical strike chance increase per power charge %': 50,
                                     'Evasion rating': 58,
                                     'Chance to evade %': 32,
                                     'Fire resistance %': 0,
                                     'Cold resistance %': 0,
                                     'Lightning resistance %': 0,
                                     'Chaos resistance %': 0,
                                     'Mana regen per second': 0.8,
                                     },
                        'Scion': {'STR': 20, 'DEX': 20, 'INT': 20,
                                  'Life': 60,
                                  'Mana': 50,
                                  'Damage per second': 4.2,
                                  'Chance to hit %': 87,
                                  'Attacks per second': 1.2,
                                  'Main hand total combined damage': '2-6',
                                  'Main hand physical damage': '2-6',
                                  'Main hand accuracy rating': 40,
                                  'Main hand critical strike damage multiplier %': 150,
                                  'Endurance charge': '0/3',
                                  'Physical damage reduction per endurance charge %': 4,
                                  'Additional elemental reduction per endurance charge %': 4,
                                  'Frenzy charges': '0/3',
                                  'Attack speed increase per frenzy charge %': 4,
                                  'Cast speed increase per frenzy charge %': 4,
                                  'Damage modifier per frenzy charge %': 4,
                                  'Power charges': '0/3',
                                  'Critical strike chance increase per power charge %': 50,
                                  'Evasion rating': 58,
                                  'Chance to evade %': 32,
                                  'Fire resistance %': 0,
                                  'Cold resistance %': 0,
                                  'Lightning resistance %': 0,
                                  'Chaos resistance %': 0,
                                  'Mana regen per second': 0.9,
                                  },
                        'Shadow': {'STR': 14, 'DEX': 23, 'INT': 23,
                                   'Life': 57,
                                   'Mana': 52,
                                   'Damage per second': 3.7,
                                   'Chance to hit %': 89,
                                   'Attacks per second': 1.2,
                                   'Main hand total combined damage': '2-5',
                                   'Main hand physical damage': '2-5',
                                   'Main hand accuracy rating': 46,
                                   'Main hand critical strike damage multiplier %': 150,
                                   'Endurance charge': '0/3',
                                   'Physical damage reduction per endurance charge %': 4,
                                   'Additional elemental reduction per endurance charge %': 4,
                                   'Frenzy charges': '0/3',
                                   'Attack speed increase per frenzy charge %': 4,
                                   'Cast speed increase per frenzy charge %': 4,
                                   'Damage modifier per frenzy charge %': 4,
                                   'Power charges': '0/3',
                                   'Critical strike chance increase per power charge %': 50,
                                   'Evasion rating': 59,
                                   'Chance to evade %': 32,
                                   'Fire resistance %': 0,
                                   'Cold resistance %': 0,
                                   'Lightning resistance %': 0,
                                   'Chaos resistance %': 0,
                                   'Mana regen per second': 0.9,
                                   },
                        'Templar': {'STR': 23, 'DEX': 14, 'INT': 23,
                                    'Life': 62,
                                    'Mana': 52,
                                    'Damage per second': 4,
                                    'Chance to hit %': 83,
                                    'Attacks per second': 1.2,
                                    'Main hand total combined damage': '2-6',
                                    'Main hand physical damage': '2-6',
                                    'Main hand accuracy rating': 28,
                                    'Main hand critical strike damage multiplier %': 150,
                                    'Endurance charge': '0/3',
                                    'Physical damage reduction per endurance charge %': 4,
                                    'Additional elemental reduction per endurance charge %': 4,
                                    'Frenzy charges': '0/3',
                                    'Attack speed increase per frenzy charge %': 4,
                                    'Cast speed increase per frenzy charge %': 4,
                                    'Damage modifier per frenzy charge %': 4,
                                    'Power charges': '0/3',
                                    'Critical strike chance increase per power charge %': 50,
                                    'Evasion rating': 58,
                                    'Chance to evade %': 32,
                                    'Fire resistance %': 0,
                                    'Cold resistance %': 0,
                                    'Lightning resistance %': 0,
                                    'Chaos resistance %': 0,
                                    'Mana regen per second': 0.9,
                                    },
                        'Duelist': {'STR': 23, 'DEX': 23, 'INT': 14,
                                    'Life': 62,
                                    'Mana': 47,
                                    'Damage per second': 4.3,
                                    'Chance to hit %': 89,
                                    'Attacks per second': 1.2,
                                    'Main hand total combined damage': '2-6',
                                    'Main hand physical damage': '2-6',
                                    'Main hand accuracy rating': 46,
                                    'Main hand critical strike damage multiplier %': 150,
                                    'Endurance charge': '0/3',
                                    'Physical damage reduction per endurance charge %': 4,
                                    'Additional elemental reduction per endurance charge %': 4,
                                    'Frenzy charges': '0/3',
                                    'Attack speed increase per frenzy charge %': 4,
                                    'Cast speed increase per frenzy charge %': 4,
                                    'Damage modifier per frenzy charge %': 4,
                                    'Power charges': '0/3',
                                    'Critical strike chance increase per power charge %': 50,
                                    'Evasion rating': 59,
                                    'Chance to evade %': 32,
                                    'Fire resistance %': 0,
                                    'Cold resistance %': 0,
                                    'Lightning resistance %': 0,
                                    'Chaos resistance %': 0,
                                    'Mana regen per second': 0.8,
                                    },
                        'Witch': {'STR': 14, 'DEX': 14, 'INT': 32,
                                  'Life': 57,
                                  'Mana': 56,
                                  'Damage per second': 3.5,
                                  'Chance to hit %': 83,
                                  'Attacks per second': 1.2,
                                  'Main hand total combined damage': '2-5',
                                  'Main hand physical damage': '2-5',
                                  'Main hand accuracy rating': 28,
                                  'Main hand critical strike damage multiplier %': 150,
                                  'Endurance charge': '0/3',
                                  'Physical damage reduction per endurance charge %': 4,
                                  'Additional elemental reduction per endurance charge %': 4,
                                  'Frenzy charges': '0/3',
                                  'Attack speed increase per frenzy charge %': 4,
                                  'Cast speed increase per frenzy charge %': 4,
                                  'Damage modifier per frenzy charge %': 4,
                                  'Power charges': '0/3',
                                  'Critical strike chance increase per power charge %': 50,
                                  'Evasion rating': 58,
                                  'Chance to evade %': 32,
                                  'Fire resistance %': 0,
                                  'Cold resistance %': 0,
                                  'Lightning resistance %': 0,
                                  'Chaos resistance %': 0,
                                  'Mana regen per second': 1,
                                  },
                        'Ranger': {'STR': 14, 'DEX': 32, 'INT': 14,
                                   'Life': 57,
                                   'Mana': 47,
                                   'Damage per second': 3.9,
                                   'Chance to hit %': 92,
                                   'Attacks per second': 1.2,
                                   'Main hand total combined damage': '2-5',
                                   'Main hand physical damage': '2-5',
                                   'Main hand accuracy rating': 64,
                                   'Main hand critical strike damage multiplier %': 150,
                                   'Endurance charge': '0/3',
                                   'Physical damage reduction per endurance charge %': 4,
                                   'Additional elemental reduction per endurance charge %': 4,
                                   'Frenzy charges': '0/3',
                                   'Attack speed increase per frenzy charge %': 4,
                                   'Cast speed increase per frenzy charge %': 4,
                                   'Damage modifier per frenzy charge %': 4,
                                   'Power charges': '0/3',
                                   'Critical strike chance increase per power charge %': 50,
                                   'Evasion rating': 59,
                                   'Chance to evade %': 32,
                                   'Fire resistance %': 0,
                                   'Cold resistance %': 0,
                                   'Lightning resistance %': 0,
                                   'Chaos resistance %': 0,
                                   'Mana regen per second': 0.8,
                                   },
                        }


def calculate_character_base_stats(character_class, character_level, character_passive_json):
    """
    Str, Dex, etc.
    """
    base_stat_json = character_class_base[character_class]
    # loop through the stuff you get for leveling
    for stat_level in character_level_bonus:
        base_stat_json[stat_level] += character_level_bonus[stat_level] * character_level
    # loop through the passive tree for base stats

    # loop through items for base stats

    return base_stat_json
