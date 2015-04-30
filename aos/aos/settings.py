"""
Django settings for aos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#BASE_DIR = os.path.dirname(os.path.dirname(__file__, ".."))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '78+m+u813esqx2&$(4+t#5b+xc_sc)b!kmi-4i-=afc!4fe3sf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'aos',
    'host',
    'servicespecific',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'xadmin',
    'crispy_forms',
    'reversion',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aos.urls'

WSGI_APPLICATION = 'aos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	    'NAME': 'aos',                      # Or path to database file if using sqlite3.
		'USER': 'root',                      # Not used with sqlite3.
		'PASSWORD': 'root',                  # Not used with sqlite3.
		'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

DATE_FORMAT = 'Y-m-d'

DATETIME_FORMAT = 'Y-m-d H:i:s'  # '2013-12-28 12:01:51'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/export/www/static/aos/'


TEMPLATE_DIRS = (
    '/export/www/aos/aos/templates/',
)

