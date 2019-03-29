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

import requests

STASH_URL_BY_ID = 'http://www.pathofexile.com/api/public-stash-tabs?id='

# TODO find 40's......for the total quality vendor recipe
# TODO Produce vendor recipe list from stashes

def com_stash_get_by_id(stash_id):
    stash_data = requests.get(STASH_URL_BY_ID + stash_id)
    return stash_data.json()


data = '2019/01/26 20:10:47 17591359 a21 [INFO Client 9756] : You have entered The Marketplace.'
newdata = (data.split('] ', 1)[1])
if newdata[0:18] == ': You have entered':
    print('ha')

