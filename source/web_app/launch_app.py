# -*- coding: utf-8 -*-


import os
import sys
# from mainapp.database import db

BASE_DIR = os.path.join(os.path.dirname(__file__))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from mainapp.app import create_app

application = create_app()
print('2hi')
# # if first user set it as administrator and create if not exists
# if os.path.isfile('/poestat/secure/db.sqlite'):
#     print('2hi2')
#     pass
# else:
#     print('2hi3')
#     db.create_all(application)
#     print('2hi4')
