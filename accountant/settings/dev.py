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
    }
}


# Debug toolbar

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}


# Emailing

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
            "level": "WARNING",
        },
        "django.request": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "propagate": False,
            "level": "WARNING",
        },

        "apps": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
    }
}
