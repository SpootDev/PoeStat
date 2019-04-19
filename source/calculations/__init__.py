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


class Calculations(object):
    """
    Main class for PoE calculations
    """

    def __init__(self, db_connection):
        self.db_connection = db_connection

    from calculations.calc_character import calculate_character_base_stats
    # from calculations.calc_items import import_base_character
    # from calculations.calc_minion import import_base_monster
    # from calculations.calc_passive import import_base_essence
    # from calculations.calc_spells import import_base_gem
    from calculations.calc_weather_poe_ninja import com_wealth_ninja_fetch_api
