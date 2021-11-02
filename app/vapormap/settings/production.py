"""
Django settings for vapormap project.

"""
from .base import *
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('VAPOR_SECRET_KEY', 'gjhliksqsdfghsdgfbhsdkjgnlkdsfj:nglbksjdhnbk')

WSGI_APPLICATION = 'vapormap.wsgi.application'

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME':  os.environ.get('VAPOR_DBNAME', 'vapordb'),
        'USER': os.environ.get('VAPOR_DBUSER', 'vaporuser'),
        'PASSWORD': os.environ.get('VAPOR_DBPASS', 'vaporpass'),
        'HOST': os.environ.get('VAPOR_DBHOST', '127.0.0.1'),
        'PORT': os.environ.get('VAPOR_DBPORT', '3306'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = './static'
