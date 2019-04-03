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

season
Optional
A particular season id. Required when type=season.

'''

import requests


def fetch_from_url(league_type='main', realm_name='pc', offset=0):
    """
    Download data from specified url
    realm_name = pc, xbox or sony
    compact = 0 - Displays the full info for leagues retrieved (will only retrieve 50 leagues)
    """
    datafile = requests.get(
        'http://api.pathofexile.com/leagues/?type=%s?compact=0?realm=%s?offset=%s',
        (league_type, realm_name, offset))
    return datafile.json()


def com_league_list():
    data_league = []
    # retrieves permanent and challenge leagues
    for league_row in fetch_from_url(league_type='main'):
        pass
    # retrieves event leagues
    for league_row in fetch_from_url(league_type='event'):
        pass
    # retrieves leagues in a particular season.
    for league_row in fetch_from_url(league_type='season'):
        # TODO if 50 leagues returned....need to grab next 50
        pass
    return data_league
