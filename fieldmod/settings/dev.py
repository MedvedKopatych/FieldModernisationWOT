from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4cf1si43$p_o5i^ck%df=n$^y2q@9@ljkf81xgrvbnyzsr=sz!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TanksBaseWOT',
        'USER': 'chieftain',
        'PASSWORD': 'Chieftain',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}



