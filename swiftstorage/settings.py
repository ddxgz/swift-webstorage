"""
Django settings for swiftstorage project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hf$!3&zy6fi4uvm9uq0zldi+jl!av*y5t2!@1r&b)h-0-l5hwc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'swiftbrowser',
    'videoplayer'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # add for swiftbrowser
    'django.middleware.http.ConditionalGetMiddleware',
)

ROOT_URLCONF = 'swiftstorage.urls'

WSGI_APPLICATION = 'swiftstorage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'America/Chicago'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    "static",
)

TEMPLATE_DIRS = (
    'templates',
    )

# Add for swiftbrowser
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# For Swift
# # for v1.0
# # SWIFT_AUTH_URL = 'http://10.200.44.66:8080/auth/v1.0'
# # for v2.0
# # SWIFT_AUTH_URL = 'http://10.200.44.66:5000/v2.0'
# SWIFT_AUTH_VERSION = 1  # 2 for keystone
# # STORAGE_URL = 'http://10.200.44.66:8080/v1/'
# # BASE_URL = 'http://10.200.44.66'  # default if using built-in runserver
# # SWAUTH_URL = 'http://10.200.44.66:8080/auth/v2'
# ALLOWED_HOSTS = ['10.200.44.66', 'swift.inesa.com']

# # for v1.0
# SWIFT_AUTH_URL = 'http://125.215.36.173:8080/auth/v1.0'
# # for v2.0
# # SWIFT_AUTH_URL = 'http://10.200.44.66:5000/v2.0'
# SWIFT_AUTH_VERSION = 1  # 2 for keystone
# STORAGE_URL = 'http://125.215.36.173:8080/v1/'
# BASE_URL = 'http://125.215.36.173'  # default if using built-in runserver
# SWAUTH_URL = 'http://125.215.36.173:8080/auth/v2'
# ALLOWED_HOSTS = ['125.215.36.173', 'swift.inesa.com']

# for v1.0
SWIFT_AUTH_URL = 'http://10.200.46.211:8080/auth/v1.0'
# for v2.0
# SWIFT_AUTH_URL = 'http://10.200.44.66:5000/v2.0'
SWIFT_AUTH_VERSION = 1  # 2 for keystone
STORAGE_URL = 'http://10.200.46.211:8080/v1/'
BASE_URL = '10.200.46.211'  # default if using built-in runserver
SWAUTH_URL = 'http://10.200.46.211:8080/auth/v2'
ALLOWED_HOSTS = ['0.0.0.0', 'insert_your_hostname_here']


SECRET_KEY = 'DONT_USE_THIS_IN_PRODUCTION'
# STATIC_URL = "http://cdnjs.cloudflare.com/ajax/libs/"

