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

import base64
import hashlib
import os
import struct
import zipfile
import zlib
from functools import reduce

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from . import common_file
from . import common_global
from . import common_hash_c_code


class CommonHashCrypto(object):
    """
    Class for interfacing with crypto
    """

    def __init__(self):
        self.hash_key = None
        self.fernet = None

    def com_hash_gen_crypt_key(self):
        if not os.path.isfile('./secure/data.zip'):
            salt = os.urandom(16)
            common_file.com_file_save_data(file_name='/poestat/secure/data.zip', data_block=salt,
                                           as_pickle=True)
        else:
            salt = common_file.com_file_load_data(file_name='/poestat/secure/data.zip', as_pickle=True)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.hash_key = base64.urlsafe_b64encode(kdf.derive(os.environ['SECURE']))
        self.fernet = Fernet(self.hash_key)

    def com_hash_gen_crypt_encode(self, encode_string):
        # encode, since it needs bytes
        return self.fernet.encrypt(encode_string.encode())

    def com_hash_gen_crypt_decode(self, decode_string):
        # encode, since it needs bytes
        # then decode, otherwise it return bytes
        return self.fernet.decrypt(decode_string.encode()).decode()
