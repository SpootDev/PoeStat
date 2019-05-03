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
http://cdn.poe.ninja/api/Data/GetDivinationCardsOverview?league=Harbinger

http://poe.ninja/api/Data/GetEssenceOverview?league=Harbinger

http://poe.ninja/api/Data/GetMapOverview?league=Harbinger

http://cdn.poe.ninja/api/Data/GetUniqueArmourOverview?league=Harbinger

http://cdn.poe.ninja/api/Data/GetUniqueFlaskOverview?league=Harbinger

http://cdn.poe.ninja/api/Data/GetUniqueWeaponOverview?league=Harbinger

http://cdn.poe.ninja/api/Data/GetUniqueAccessoryOverview?league=Harbinger

http://cdn.poe.ninja/api/Data/GetUniqueJewelOverview?league=Harbinger

http://poe.ninja/api/Data/GetFragmentOverview?league=Harbinger

http://poe.ninja/api/Data/GetProphecyOverview?league=Harbinger

http://cdn.poe.ninja/api/Data/GetUniqueMapOverview?league=Harbinger

# give stats on how much they've processed
http://poe.ninja/api/Data/GetStats
'''

import json
import requests


def com_wealth_ninja_fetch_api(self, league_name='Standard'):
    with requests.Session() as char_session:
        response = char_session.post(
            'http://poe.ninja/api/Data/GetCurrencyOverview?league=%s' % league_name)
        return json.loads(response.content)
