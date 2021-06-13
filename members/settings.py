"""
Django settings for members project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=True
if 'ENVIRONMENT' in os.environ and os.environ['ENVIRONMENT'] != 'development':
    DEBUG = False

__server_host_url = os.environ['SERVER_PROTOCOL'] + '://' + os.environ['SERVER_HOSTNAME']
if 'SERVER_PORT' in os.environ:
    __server_host_url += ':' + os.environ['SERVER_PORT']

ALLOWED_HOSTS = [
    os.environ['SERVER_HOSTNAME']
]

WEBAPP_URL_BASE=__server_host_url

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.admindocs',

    # Libraries
    'django_filters',
    'phonenumber_field',
    'localflavor',
    'crispy_forms',
    'django_bootstrap_breadcrumbs',

    # API Stuff
    'rest_framework',
    'rest_framework.authtoken',

    # Mine
    'membership.apps.MembershipConfig',
    'management.apps.ManagementConfig',
    'api.apps.ApiConfig',
    'keyfobs.apps.KeyfobsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'members.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'members.wsgi.application'

AUTH_USER_MODEL='management.User'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']

MANAGERS = os.environ['MANAGER_EMAILS'].split(',')
# get rid of trailing '' if there's only one manager
if len(MANAGERS) > 1 and MANAGERS[-1] == '':
    MANAGERS.pop()


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'management.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

#### Heroku ####
import django_heroku
django_heroku.settings(locals())

# Hack to get PostgreSQL to work on localhost
if os.environ['SERVER_HOSTNAME'] == 'localhost':
    del DATABASES['default']['OPTIONS']['sslmode']

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
