"""
WSGI config for vapormap project.

"""

import os
import sys
import configparser
from django.core.wsgi import get_wsgi_application

config = configparser.ConfigParser()
# Retrieve configuration from /etc/vapormap.ini
# Set them to environment variables for process group
try:
	appconf = config.read('/etc/vapormap.ini')
except:
	sys.exit(0)

for k in config['configuration']:
	os.environ[k.upper()] = config['configuration'][k]

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vapormap.settings.production')

application = get_wsgi_application()
