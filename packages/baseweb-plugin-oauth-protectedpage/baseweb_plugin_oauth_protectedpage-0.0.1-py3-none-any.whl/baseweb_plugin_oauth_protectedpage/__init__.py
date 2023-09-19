__version__ = "0.0.1"

# set up server side infrastructure

from . import auth

# set up client side infrastructure

import os
from baseweb.interface import register_component

register_component("protectedpage.js", os.path.dirname(__file__))
register_component("auth.js", os.path.dirname(__file__))
