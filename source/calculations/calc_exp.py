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

import math

# Level Total XP    XP to Gain
character_level_tiers = {
    1: {'Total': 0, 'Gain': 525},
    2: {'Total': 525, 'Gain': 1235},
    3: {'Total': 1760, 'Gain': 2021},
    4: {'Total': 3781, 'Gain': 3403},
    5: {'Total': 7184, 'Gain': 5002},
    6: {'Total': 12186, 'Gain': 7138},
    7: {'Total': 19324, 'Gain': 10053},
    8: {'Total': 29377, 'Gain': 13804},
    9: {'Total': 43181, 'Gain': 18512},
    10: {'Total': 61693, 'Gain': 24297},
    11: {'Total': 85990, 'Gain': 31516},
    12: {'Total': 117506, 'Gain': 39878},
    13: {'Total': 157384, 'Gain': 50352},
    14: {'Total': 207736, 'Gain': 62261},
    15: {'Total': 269997, 'Gain': 76465},
    16: {'Total': 346462, 'Gain': 92806},
    17: {'Total': 439268, 'Gain': 112027},
    18: {'Total': 551295, 'Gain': 133876},
    19: {'Total': 685171, 'Gain': 158538},
    20: {'Total': 843709, 'Gain': 187025},
    21: {'Total': 1030734, 'Gain': 218895},
    22: {'Total': 1249629, 'Gain': 255366},
    23: {'Total': 1504995, 'Gain': 295852},
    24: {'Total': 1800847, 'Gain': 341805},
    25: {'Total': 2142652, 'Gain': 392470},
    26: {'Total': 2535122, 'Gain': 449555},
    27: {'Total': 2984677, 'Gain': 512121},
    28: {'Total': 3496798, 'Gain': 583857},
    29: {'Total': 4080655, 'Gain': 662181},
    30: {'Total': 4742836, 'Gain': 747411},
    31: {'Total': 5490247, 'Gain': 844146},
    32: {'Total': 6334393, 'Gain': 949053},
    33: {'Total': 7283446, 'Gain': 1064952},
    34: {'Total': 8384398, 'Gain': 1192712},
    35: {'Total': 9541110, 'Gain': 1333241},
    36: {'Total': 10874351, 'Gain': 1487491},
    37: {'Total': 12361842, 'Gain': 1656447},
    38: {'Total': 14018289, 'Gain': 1841143},
    39: {'Total': 15859432, 'Gain': 2046202},
    40: {'Total': 17905634, 'Gain': 2265837},
    41: {'Total': 20171471, 'Gain': 2508528},
    42: {'Total': 22679999, 'Gain': 2776124},
    43: {'Total': 25456123, 'Gain': 3061734},
    44: {'Total': 28517857, 'Gain': 3379914},
    45: {'Total': 31897771, 'Gain': 3723676},
    46: {'Total': 35621447, 'Gain': 4099570},
    47: {'Total': 39721017, 'Gain': 4504444},
    48: {'Total': 44225461, 'Gain': 4951099},
    49: {'Total': 49176560, 'Gain': 5430907},
    50: {'Total': 54607467, 'Gain': 5957868},
    51: {'Total': 60565335, 'Gain': 6528910},
    52: {'Total': 67094245, 'Gain': 7153414},
    53: {'Total': 74247659, 'Gain': 7827968},
    54: {'Total': 82075627, 'Gain': 8555414},
    55: {'Total': 90631041, 'Gain': 9353933},
    56: {'Total': 99984974, 'Gain': 10212541},
    57: {'Total': 110197515, 'Gain': 11142646},
    58: {'Total': 121340161, 'Gain': 12157041},
    59: {'Total': 133497202, 'Gain': 13252160},
    60: {'Total': 146749362, 'Gain': 14441758},
    61: {'Total': 161191120, 'Gain': 15731508},
    62: {'Total': 176922628, 'Gain': 17127265},
    63: {'Total': 194049893, 'Gain': 18635053},
    64: {'Total': 212684946, 'Gain': 20271765},
    65: {'Total': 232956711, 'Gain': 22044909},
    66: {'Total': 255001620, 'Gain': 23950783},
    67: {'Total': 278952403, 'Gain': 26019833},
    68: {'Total': 304972236, 'Gain': 28261412},
    69: {'Total': 333233648, 'Gain': 30672515},
    70: {'Total': 363906163, 'Gain': 33287878},
    71: {'Total': 397194041, 'Gain': 36118904},
    72: {'Total': 433312945, 'Gain': 39163425},
    73: {'Total': 472476370, 'Gain': 42460810},
    74: {'Total': 514937180, 'Gain': 46024718},
    75: {'Total': 560961898, 'Gain': 49853964},
    76: {'Total': 610815862, 'Gain': 54008554},
    77: {'Total': 664824416, 'Gain': 58473753},
    78: {'Total': 723298169, 'Gain': 63314495},
    79: {'Total': 786612664, 'Gain': 68516464},
    80: {'Total': 855129128, 'Gain': 74132190},
    81: {'Total': 929261318, 'Gain': 80182477},
    82: {'Total': 1009443795, 'Gain': 86725730},
    83: {'Total': 1096169525, 'Gain': 93748717},
    84: {'Total': 1189918242, 'Gain': 101352108},
    85: {'Total': 1291270350, 'Gain': 109524907},
    86: {'Total': 1400795257, 'Gain': 118335069},
    87: {'Total': 1519130326, 'Gain': 127813148},
    88: {'Total': 1646943474, 'Gain': 138033822},
    89: {'Total': 1784977296, 'Gain': 149032822},
    90: {'Total': 1934009687, 'Gain': 160890604},
    91: {'Total': 2094900291, 'Gain': 173648795},
    92: {'Total': 2268549086, 'Gain': 187372170},
    93: {'Total': 2455921256, 'Gain': 202153736},
    94: {'Total': 2658074992, 'Gain': 218041909},
    95: {'Total': 2876116901, 'Gain': 235163399},
    96: {'Total': 3111280300, 'Gain': 253547862},
    97: {'Total': 3364828162, 'Gain': 273358532},
    98: {'Total': 3638186694, 'Gain': 294631836},
    99: {'Total': 3932818530, 'Gain': 317515914},
    100: {'Total': 4250334444, 'Gain': 0},
}

monster_level_mods = {
    70: {'Tier': 3, 'Level': 70},
    71: {'Tier': 4, 'Level': 70.94},
    72: {'Tier': 5, 'Level': 71.82},
    73: {'Tier': 6, 'Level': 72.64},
    74: {'Tier': 7, 'Level': 73.40},
    75: {'Tier': 8, 'Level': 74.10},
    76: {'Tier': 9, 'Level': 74.74},
    77: {'Tier': 10, 'Level': 75.32},
    78: {'Tier': 11, 'Level': 75.84},
    79: {'Tier': 12, 'Level': 76.30},
    80: {'Tier': 13, 'Level': 76.70},
    81: {'Tier': 14, 'Level': 77.04},
    82: {'Tier': 15, 'Level': 77.32},
    83: {'Tier': -1, 'Level': 77.54},
    84: {'Tier': -1, 'Level': 77.70},
}


def calc_exp_by_level(character_level, area_level):
    # determine area_level mods for monster level
    if area_level >= 70:
        area_level = monster_level_mods[area_level]['Level']
    # find the "safezone"
    safezone = math.floor(3 + (character_level / 16))
    # calc the effective difference
    effective_difference = max(abs(character_level - area_level) - safezone, 0)
    print(safezone, effective_difference)
    # check for 95 or higher
    if character_level >= 95:
        final_exp = max((((character_level + 5) / (
                character_level + 5 + (effective_difference ** 2.5))) ** 1.5) * (
                                1 / (1 + 0.1 * (character_level - 94))), 0.01)
    else:
        final_exp = max((((character_level + 5) / (
                character_level + 5 + (effective_difference ** 2.5))) ** 1.5), 0.01)
    return final_exp * 100
