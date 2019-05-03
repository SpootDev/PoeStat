# -*- coding: utf-8 -*-


import os
import sys

BASE_DIR = os.path.join(os.path.dirname(__file__))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from mainapp.app import create_app
from common import common_global
from common import common_logging_elasticsearch


application = create_app()
