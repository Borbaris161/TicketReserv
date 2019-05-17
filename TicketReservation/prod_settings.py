# coding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cinema_db',
        'USER': 'borbaris161',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_db',
        },
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'