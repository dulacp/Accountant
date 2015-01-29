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


# Security

ALLOWED_HOSTS = (
    '.herokuapp.com',  # Prefer an url with no subdomain authorized
)


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
    },
    "loggers": {
        "django": {
            "handlers": ["console"],  # "null"
            "propagate": True,
            "level": "WARNING",
        },
        "django.request": {
            "handlers": ["console"],
            "level": "WARNING",  # "ERROR"
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
