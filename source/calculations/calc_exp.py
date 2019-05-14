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
character_level_teirs = {
    1: {'Total': 0, 'Gain': 525},
        51: {'Total': 60565335, 'Gain': 6528910},
2: {'Total': 525, 'Gain': 	1,235},
52: {'Total': 67,094,245, 'Gain': 	7,153,414},
3: {'Total': 1,760, 'Gain': 	2,021},
53: {'Total': 74,247,659, 'Gain': 	7,827,968},
4: {'Total': 3,781	, 'Gain': 3,403},
54: {'Total': 82,075,627, 'Gain': 	8,555,414},
5: {'Total': 7,184, 'Gain': 	5,002},
55: {'Total': 90,631,041, 'Gain': 	9,353,933},
6: {'Total': 12,186	, 'Gain': 7,138},
56: {'Total': 99,984,974, 'Gain': 	10,212,541},
7: {'Total': 19,324, 'Gain': 	10,053},
57: {'Total': 110,197,515, 'Gain': 	11,142,646},
8: {'Total': 29,377, 'Gain': 	13,804},
58: {'Total': 121,340,161, 'Gain': 	12,157,041},
9: {'Total': 43,181	, 'Gain': 18,512},
59: {'Total': 133,497,202, 'Gain': 	13,252,160},
10: {'Total': 61,693, 'Gain': 	24,297},
60: {'Total': 146,749,362, 'Gain': 	14,441,758},
11: {'Total': 85,990, 'Gain': 	31,516},
61: {'Total': 161,191,120, 'Gain': 	15,731,508},
12: {'Total': 117,506, 'Gain': 	39,878},
62: {'Total': 176,922,628, 'Gain': 	17,127,265},
13: {'Total': 157,384	, 'Gain': 50,352},
63: {'Total': 194,049,893, 'Gain': 	18,635,053},
14: {'Total': 	207,736, 'Gain': 	62,261},
64: {'Total': 212,684,946	, 'Gain': 20,271,765},
15: {'Total': 	269,997, 'Gain': 	76,465},
65: {'Total': 	232,956,711, 'Gain': 	22,044,909},
16: {'Total': 	346,462	, 'Gain': 92,806},
66: {'Total': 	255,001,620, 'Gain': 	23,950,783},
17: {'Total': 	439,268, 'Gain': 	112,027},
67: {'Total': 	278,952,403, 'Gain': 	26,019,833},
18: {'Total': 	551,295	, 'Gain': 133,876},
68: {'Total': 	304,972,236, 'Gain': 	28,261,412},
19: {'Total': 	685,171	, 'Gain': 158,538},
69: {'Total': 	333,233,648, 'Gain': 	30,672,515},
20: {'Total': 	843,709, 'Gain': 	187,025},
70: {'Total': 	363,906,163, 'Gain': 	33,287,878},
21: {'Total': 	1,030,734, 'Gain': 	218,895},
71: {'Total': 	397,194,041	, 'Gain': 36,118,904},
22: {'Total': 	1,249,629, 'Gain': 	255,366},
72: {'Total': 	433,312,945, 'Gain': 	39,163,425},
23: {'Total': 	1,504,995, 'Gain': 	295,852},
73: {'Total': 	472,476,370, 'Gain': 	42,460,810},
24: {'Total': 	1,800,847	, 'Gain': 341,805},
74: {'Total': 	514,937,180, 'Gain': 	46,024,718},
25: {'Total': 	2,142,652, 'Gain': 	392,470},
75: {'Total': 	560,961,898, 'Gain': 	49,853,964},
26: {'Total': 	2,535,122	, 'Gain': 449,555},
76: {'Total': 	610,815,862, 'Gain': 	54,008,554},
27: {'Total': 	2,984,677, 'Gain': 	512,121},
77: {'Total': 	664,824,416, 'Gain': 	58,473,753},
28: {'Total': 	3,496,798	, 'Gain': 583,857},
78: {'Total': 	723,298,169	, 'Gain': 63,314,495},
29: {'Total': 	4,080,655, 'Gain': 	662,181},
79: {'Total': 	786,612,664, 'Gain': 	68,516,464},
30: {'Total': 	4,742,836	, 'Gain': 747,411},
80: {'Total': 	855,129,128, 'Gain': 	74,132,190},
31: {'Total': 	5,490,247	, 'Gain': 844,146},
81: {'Total': 	929,261,318, 'Gain': 	80,182,477},
32: {'Total': 	6,334,393	, 'Gain': 949,053},
82: {'Total': 	1,009,443,795, 'Gain': 	86,725,730},
33: {'Total': 	7,283,446, 'Gain': 	1,064,952},
83: {'Total': 	1,096,169,525, 'Gain': 	93,748,717},
34: {'Total': 	8,384,398, 'Gain': 	1,192,712},
84: {'Total': 	1,189,918,242, 'Gain': 	101,352,108},
35: {'Total': 	9,541,110, 'Gain': 	1,333,241},
85: {'Total': 	1,291,270,350, 'Gain': 	109,524,907},
36: {'Total': 	10,874,351, 'Gain': 	1,487,491},
86: {'Total': 	1,400,795,257, 'Gain': 	118,335,069},
37: {'Total': 	12,361,842, 'Gain': 	1,656,447},
87: {'Total': 	1,519,130,326, 'Gain': 	127,813,148},
38: {'Total': 	14,018,289, 'Gain': 	1,841,143},
88: {'Total': 	1,646,943,474, 'Gain': 	138,033,822},
39: {'Total': 	15,859,432, 'Gain': 	2,046,202},
89: {'Total': 	1,784,977,296	, 'Gain': 149,032,822},
40: {'Total': 	17,905,634, 'Gain': 	2,265,837},
90: {'Total': 	1,934,009,687, 'Gain': 	160,890,604},
41: {'Total': 	20,171,471, 'Gain': 	2,508,528},
91: {'Total': 	2,094,900,291, 'Gain': 	173,648,795},
42: {'Total': 	22,679,999, 'Gain': 	2,776,124},
92: {'Total': 	2,268,549,086, 'Gain': 	187,372,170},
43: {'Total': 	25,456,123, 'Gain': 	3,061,734},
93: {'Total': 	2,455,921,256, 'Gain': 	202,153,736},
44: {'Total': 	28,517,857, 'Gain': 	3,379,914},
94: {'Total': 	2,658,074,992, 'Gain': 	218,041,909},
45: {'Total': 	31,897,771, 'Gain': 	3,723,676},
95: {'Total': 	2,876,116,901, 'Gain': 	235,163,399},
46: {'Total': 	35,621,447, 'Gain': 	4,099,570},
96: {'Total': 	3,111,280,300, 'Gain': 	253,547,862},
47: {'Total': 	39,721,017, 'Gain': 	4,504,444},
97: {'Total': 	3,364,828,162, 'Gain': 	273,358,532},
48: {'Total': 	44,225,461, 'Gain': 	4,951,099},
98: {'Total': 	3,638,186,694, 'Gain': 	294,631,836},
49: {'Total': 	49,176,560, 'Gain': 	5,430,907},
99: {'Total': 	3,932,818,530, 'Gain': 	317,515,914},
50: {'Total': 	54,607,467	, 'Gain': 5,957,868},
100: {'Total': 	4,250,334,444, 'Gain': 	0},
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
