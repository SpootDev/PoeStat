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

# TODO for alerts.....do the OS alert as well?

# TODO add chat records to database from client.txt

# TODO alert on trade messages
## for sniping add to clipboard automatically - might need xclip in linux installed
## toClip = "@%s Hi I would like to buy your %s listed for %s" %(x['accountName'], y['typeLine'], y['note'])
## pyperclip.copy(toClip)

# TODO alert on whisper messages
# chat.startswith("@From")