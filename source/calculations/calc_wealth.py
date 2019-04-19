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


def com_wealth_stash(self, account_uuid, league_name='Standard'):
    # currencyTypeName, chaosEquivalent - in the ninja json
    ninja_currency = self.db_connection.db_wealth_poe_ninja_currency_read(league_name)
    total_wealth = 0
    for item_info in self.db_connection.db_item_account_list(account_uuid):
        print(item_info)
        if 'notes' in item_info:
            # use the price the person has listed
            pass
        else:
            # if currency type hit poe ninja currency table
            if item_info['typeLine'] in ninja_currency:
                total_wealth += item_info['stackSize'] \
                                * ninja_currency[item_info['typeLine']['chaosEquivalent']]
            else:
                # lookup price in orders
                pass
    return total_wealth
