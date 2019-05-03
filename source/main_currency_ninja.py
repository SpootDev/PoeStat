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

import calculations as calculations_base
import database as database_base

# open up the database
db_connection = database_base.ServerDatabase()
db_connection.db_open()

calc_inst = calculations_base.Calculations(db_connection)
db_connection.db_wealth_poe_ninja_currency_write(calc_inst.com_wealth_ninja_fetch_api())

# commit
db_connection.db_commit()

# close the database
db_connection.db_close()
