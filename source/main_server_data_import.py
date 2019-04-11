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
This program will be used to import/update the data from RePoE from Github.
'''

import database as database_base
import dataimport as dataimport_base

# open up the database
db_connection = database_base.ServerDatabase()
db_connection.db_open()

# setup the import for base item classes
import_inst = dataimport_base.ServerImport(db_connection)
class_uuid_array = import_inst.import_base_class_items()

# this will process the base_items.json which will be subtype of classes above
import_inst.import_base_items(class_uuid_array)

# close the database
db_connection.db_close()
