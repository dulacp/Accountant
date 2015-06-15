from os import environ
from os.path import dirname, join

from .common import *

import dj_database_url
from boto.s3.connection import SubdomainCallingFormat


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


# Storage

# use Amazon S3 for storage for uploaded media files and static files
DEFAULT_FILE_STORAGE = 'accountant.s3_storages.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'accountant.s3_storages.StaticRootS3BotoStorage'


# Amazon S3

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_S3_CALLING_FORMAT = SubdomainCallingFormat()

AWS_ACCESS_KEY_ID = environ.get("AWS_S3_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = environ.get("AWS_S3_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = environ.get("AWS_STORAGE_BUCKET_NAME", "")

AWS_HOST = environ.get("AWS_S3_HOST", "s3.amazonaws.com")
AWS_AUTO_CREATE_BUCKET = False
AWS_S3_FILE_OVERWRITE = False
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
AWS_REDUCED_REDUNDANCY = False

# AWS cache settings, don't change unless you know what you're doing
AWS_IS_GZIPPED = True
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'public, max-age=%d' % AWS_EXPIREY
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME


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
