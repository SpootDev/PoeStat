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


def com_char_get_list(account_name, league_name=None):
    # https://www.pathofexile.com/character-window/get-characters?accountName=spooticusmaximus
    poe_char_request = requests.get(
        'https://www.pathofexile.com/character-window/get-characters?accountName=%s' % account_name)
    if poe_char_request.status_code == 200:
        result_data = poe_char_request.json()
        if 'error' in result_data:
            return None
        else:
            if league_name is not None:
                character_list = []
                for character_data in result_data:
                    if character_data['league'] == league_name:
                        character_list.append(character_data)
            else:
                return result_data
    return None

# https://www.pathofexile.com/account/view-profile/spooticusmaximus
# can use to get guild and stuff with bsoup
# https://www.pathofexile.com/account/view-profile/Blocknite/characters - full blown gui web list
# if errMsg == "Response code: 403" then
#     "Account profile is private."
# elseif errMsg == "Response code: 404" then
#     "Account name is incorrect."
