"""
Django settings for omega_champions project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from pyrebase import pyrebase

from core.utils import dev_template_config, prod_template_config

gettext = lambda s: s

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DJANGO_DEBUG', 'True') == 'True')
if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['http://5.189.132.142']

# Application definition

firebaseConfig = {
    'apiKey': "AIzaSyCA0SsSAfdhJeoywB6gFzHPgAe_EKas9R4",
    'authDomain': "teamup-1c4d5.firebaseapp.com",
    'projectId': "teamup-1c4d5",
    'storageBucket': "teamup-1c4d5.appspot.com",
    'databaseURL': "https://teamup-1c4d5-default-rtdb.firebaseio.com/",
    'messagingSenderId': "591293928733",
    'appId': "1:591293928733:web:0da8770145ee22cf6d3df4",
    'measurementId': "G-3G8R9DZ64K"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders'
]

INNER_APPS = [
    'apps.NepalAdministrativeDivision',
    'apps.Address',
    'apps.Organization',
    'apps.Skill',
    'apps.Room',
    'apps.Tool',
]

THIRD_PARTY_APPS = [
    'gettext',
    'rest_framework',
    'rest_framework.authtoken'
]

INSTALLED_APPS += INNER_APPS
INSTALLED_APPS += THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

ROOT_URLCONF = 'teamup_web.urls'

if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True

if os.environ.get('DJANGO_DEBUG', 'True') == 'True':
    TEMPLATES = [dev_template_config]
else:
    TEMPLATES = [prod_template_config]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        'HOST': os.environ.get("SQL_HOST", "localhost"),
        'NAME': os.environ.get("SQL_PASSWORD", "postgres"),
        'PASSWORD': os.environ.get("SQL_PASSWORD", "postgres"),
        'PORT': os.environ.get("SQL_PORT", "5432"),
        'USER': os.environ.get("SQL_USER", "postgres"),
    }
}

WSGI_APPLICATION = 'core.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
CSRF_TRUSTED_ORIGINS = [
    'http://5.189.132.142:2023'
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = (
    ## Customize this
    ('ne', gettext('ne')),
    ('en', gettext('en'))
)
DEFAULT_LANGUAGE = 1
LANGUAGE_CODE = 'ne'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PARLER_LANGUAGES = {
    None: (
        {'code': 'en', },
        {'code': 'ne', },

    ),
    'default': {
        'fallbacks': ['ne'],  # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,  # the default; let .active_translations() return fallbacks too.
    }
}

LANGUAGES = (
    ('en', _("English")),
    ('ne', _("Nepali")),
)

PARLER_DEFAULT_LANGUAGE_CODE = 'ne'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

X_FRAME_OPTIONS = 'SAMEORIGIN'

WEBPACK_LOADER = {
    'DEFAULT': {
        'STATS_FILE': os.path.join(BASE_DIR, 'static', 'webpack-stats.json'),
    },
}

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media/')

STATIC_URL = '/public/'
# use in deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'core', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'assets'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = '/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser'
    ),
}

if DEBUG:
    CORS_ORIGIN_WHITELIST = ['http://localhost:4000']
else:
    CORS_ORIGIN_WHITELIST = ['http://5.189.132.142']
