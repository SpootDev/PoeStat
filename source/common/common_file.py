'''
  Copyright (C) 2015 Quinn D Granfor <spootdev@gmail.com>

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

import os
import pickle
import time


def com_file_save_data(file_name, data_block, as_pickle=False, with_timestamp=False,
                       file_ext=None):
    """
    Save data as file
    """
    file_handle = None
    if as_pickle:
        write_type = 'wb'
    else:
        write_type = 'w+'
    if with_timestamp:
        file_handle = open(file_name + '_' +
                           time.strftime("%Y%m%d%H%M%S") + file_ext, write_type)
    else:
        file_handle = open(file_name, write_type)
    if as_pickle:
        pickle.dump(data_block, file_handle)
    else:
        file_handle.write(data_block)
    file_handle.close()


def com_file_load_data(file_name, as_pickle=False):
    """
    Load data from file as ascii or pickle
    """
    if as_pickle:
        read_type = 'rb'
    else:
        read_type = 'r'
    file_handle = open(file_name, read_type)
    if as_pickle:
        data_block = pickle.loads(file_handle.read())
    else:
        data_block = file_handle.read()
    file_handle.close()
    return data_block


def com_mkdir_p(filename):
    """
    create directory path if not exists
    """
    try:
        folder = os.path.dirname(filename)
        if not os.path.exists(folder):
            os.makedirs(folder)
        return True
    except:
        return False
