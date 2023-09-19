# load the environment variables for this setup from .env file
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True))
load_dotenv(find_dotenv(".env.local"))

# load the plugin (before exposing the server, to allow for proper init)

import baseweb_plugin_oauth_protectedpage

# expose "server" to allow for "gunicorn -k eventlet -w 1 app:server" execution

from baseweb.web import server

import os

server.config["TEMPLATES_AUTO_RELOAD"] = True
server.config["SECRET_KEY"] = os.environ.get("APP_SECRET_KEY", default="local")

# setup a fake, local, in-memory, minimalistic mongo instance and provide it
# to the plugin

import fake_mongo

baseweb_plugin_oauth_protectedpage.auth.db.mongoclient = fake_mongo.FakeMongo()

# register two pages

HERE = os.path.dirname(__file__)

from baseweb.interface import register_component, register_static_folder

register_static_folder(os.path.join(HERE, "static"))

register_component("unprotected.js", HERE)
register_component("protected.js",   HERE)
