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
import requests


def com_char_get_stash(poe_session_id, account_name, account_league, tab_ndx):
    with requests.Session() as char_session:
        response = char_session.post(
            'https://pathofexile.com/character-window/get-stash-items?accountName=%s&league=Standard&tabIndex=1&tabs=1' % account_name,
            headers={'Cookie': 'POESESSID=' + poe_session_id})
        content = json.loads(response.content)


# TODO Generate Path of Building definitions


def com_char_get_list(account_name, league_name):
    pass