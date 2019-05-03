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


# the stash index's start at 0
def com_char_get_stash(poe_session_id, account_name, account_league, tab_ndx):
    with requests.Session() as char_session:
        response = char_session.post(
            'https://pathofexile.com/character-window/get-stash-items?accountName=%s&league=%s&tabIndex=%s&tabs=1' % (
                account_name, account_league, tab_ndx),
            headers={'Cookie': 'POESESSID=' + poe_session_id})
        return json.loads(response.content)


# TODO Generate Path of Building definitions


def com_char_get_list(account_name, league_name=None):
    """
    [{"name":"Fake","league":"Standard","classId":6,"ascendancyClass":0,
    `   "class":"Shadow","level":75,"experience":566277952}]
    """
    poe_char_request = requests.get(
        'https://www.pathofexile.com/character-window/get-characters?accountName=%s' % account_name,
        headers={'accept-encoding': 'gzip'})
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
                return character_list
            else:
                return result_data
    return None


def com_char_get_passive(poe_session_id, account_name, character_name, realm_code='pc'):
    with requests.Session() as char_session:
        response = char_session.post(
            'https://www.pathofexile.com/character-window/get-passive-skills?accountName=%s&character=%s&realm=%s' % (
                account_name, character_name, realm_code),
            headers={'Cookie': 'POESESSID=' + poe_session_id})
        return json.loads(response.content)


def com_char_get_items(poe_session_id, account_name, character_name, realm_code='pc'):
    with requests.Session() as char_session:
        response = char_session.post(
            'https://www.pathofexile.com/character-window/get-items?accountName=%s&character=%s&realm=%s' % (
                account_name, character_name, realm_code),
            headers={'Cookie': 'POESESSID=' + poe_session_id})
        return json.loads(response.content)

# https://www.pathofexile.com/account/view-profile/spooticusmaximus
# can use to get guild and stuff with bsoup
# https://www.pathofexile.com/account/view-profile/Blocknite/characters - full blown gui web list
# if errMsg == "Response code: 403" then
#     "Account profile is private."
# elseif errMsg == "Response code: 404" then
#     "Account name is incorrect."


# print(com_char_get_passive(poe_session_id='',
#                            account_name='spooticusmaximus',
#                            character_name='DarkKittySpoo', realm_code='pc'))

# print(com_char_get_stash(poe_session_id='',
#                          account_name='spooticusmaximus',
#                          account_league='Standard', tab_ndx=0))
