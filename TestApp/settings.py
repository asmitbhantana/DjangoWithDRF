"""
Django settings for TestApp project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import export as export

import TestApp

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cxzkx7bmo+tu4$(nljwms17p=5+$z)=i&^f%9$34b)w8v-wyx('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstApp',
    'modelExtra',
    'templating',
    'formApp',
    'mediaFile',
    'middlewareApp',
    'crudApp',
    'accounts',
    'user',
    'classbased',
    'statusapp',

    'debug_toolbar',
    'django_extensions',
    'restApp',
    'rest_framework',
    'rest_framework.authtoken',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'TestApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'TestApp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'prod-static')
# .manage.py collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# mail settings
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '6f65a4fad2768f'
EMAIL_HOST_PASSWORD = 'cdc029fc9dba0e'
EMAIL_PORT = '2525'
# use send_email method
# create templates and use send_template like method to send the emails

# for caches use {% cache load %} {% cache 200 body request.user %}
# for views use @cache_page(time in seconds) deorators
CACHES = {
    'default': {  # for database cache
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'CACHE_TABLE'
    },
    # 'default': {  # for file based cache
    #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #     'LOCATION': os.path.join(BASE_DIR, "cache_file")
    # }
}

# for custom user model
AUTH_USER_MODEL = 'user.User'