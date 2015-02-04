from os import environ
from os.path import dirname, join

from .common import *

import dj_database_url


DEBUG = False
TEMPLATE_DEBUG = False
LOCAL_SERVER = bool(int(environ.get('LOCAL_SERVER', '1')))

# load local .env
if LOCAL_SERVER:
    import dotenv
    PROJECT_PATH = dirname(dirname(dirname(__file__)))
    dotenv.load_dotenv(join(PROJECT_PATH, ".env"))


# Database

DATABASES = {
    'default': dj_database_url.config(default='')
}


# Apps

INSTALLED_APPS = INSTALLED_APPS + (
    # Sentry exception capturing
    'raven.contrib.django.raven_compat',
)


# Security

ALLOWED_HOSTS = (
    '.herokuapp.com',  # Prefer an url with no subdomain authorized
)

SITE_MAIN_DOMAIN = environ.get('SITE_MAIN_DOMAIN', '')
SITE_MAIN_NAME = environ.get('SITE_MAIN_NAME', SITE_MAIN_DOMAIN)


# Emailing

MANDRILL_API_KEY = environ.get('MANDRILL_APIKEY', '')
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "sentry": {
            "level": "WARNING",
            "class": "raven.contrib.django.handlers.SentryHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "sentry"],  # "null"
            "propagate": True,
            "level": "WARNING",
        },
        "django.request": {
            "handlers": ["console", "sentry"],
            "level": "WARNING",  # "ERROR"
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console", "sentry"],
            "propagate": False,
            "level": "WARNING",
        },

        "apps": {
            "handlers": ["console", "sentry"],
            "level": "WARNING",
            "propagate": False,
        },
    }
}


# Sentry

RAVEN_CONFIG = {
    "dsn": environ.get("RAVEN_DNS", "")
}
