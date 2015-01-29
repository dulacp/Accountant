"""
Django settings for accountant project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import sys
from decimal import Decimal

import accounting


VERSION = accounting.VERSION
DISPLAY_VERSION = accounting.get_version()
DISPLAY_SHORT_VERSION = accounting.get_short_version()


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.basename(BASE_DIR)

# Add the BASE_DIR to the path in order to reuse the apps easily
sys.path.append(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o7k)j*lewj6va4yqz=#1^z@6wtf!$#dx(u=z!3(351rc27c9fm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOCAL_SERVER = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'djrill',
    'crispy_forms',
    'avatar',  # for user avatars
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'stronghold',  # enforce login on the whole app
)

# Accounting apps
from accounting import get_apps
LOCAL_APPS = get_apps()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# Migrations

MIGRATION_MODULES = {
    'sites': 'migrations.sites',
    'socialaccount': 'migrations.socialaccount',
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'stronghold.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'accountant.urls'

WSGI_APPLICATION = 'accountant.wsgi.application'


# Emailing

DEFAULT_FROM_EMAIL = 'noreply@accountant.fr'


# Templates
# https://docs.djangoproject.com/en/1.7/ref/settings/#template-context-processors
from accounting import ACCOUNTING_TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',

    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',

    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
) + ACCOUNTING_TEMPLATE_CONTEXT_PROCESSORS

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#template-dirs
from accounting import ACCOUNTING_MAIN_TEMPLATE_DIR
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    ACCOUNTING_MAIN_TEMPLATE_DIR,
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': ''
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# See: https://docs.djangoproject.com/en/1.7/ref/contrib/staticfiles\
#      /#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",

    "djangobower.finders.BowerFinder",
)


# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Bower config

BOWER_COMPONENTS_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'components'))

BOWER_INSTALLED_APPS = (
    'modernizr',
    'jquery',
    'bootstrap',
)


# Custom User

LOGIN_REDIRECT_URL = 'connect:getting-started'
LOGIN_URL = 'account_login'


# Authentication

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


# Stronghold

STRONGHOLD_PUBLIC_URLS = (
    r'^%s.+$' % STATIC_URL,
    r'^%s.+$' % MEDIA_URL,
    r'^/accounts/.*$',
)
STRONGHOLD_PUBLIC_NAMED_URLS = (
)


# Forms

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Accounting

from accounting.defaults import *
