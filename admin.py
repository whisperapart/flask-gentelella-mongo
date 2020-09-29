from os import environ
from sys import exit

from config import config_dict
from app import create_app


get_config_mode = environ.get('GENTELELLA_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid GENTELELLA_CONFIG_MODE environment variable entry.')

config_mode.MONGO_URI = "mongodb://10.37.129.100:27017/x0050"
config_mode.JSON_AS_ASCII = False
app = create_app(config_mode)
