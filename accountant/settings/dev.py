import os

from .common import *


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'accountant',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'autocommit': True,
        },
    }
}


# Debug toolbar

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)


# Emailing

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
