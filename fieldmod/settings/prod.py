import django_on_heroku
from decouple import config

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost',
                                      engine='django.db.backends.postgresql_psycopg2',
                                      conn_max_age=600, ssl_require=False)
}

ALLOWED_HOSTS = [
    'field-modernization-wot.herokuapp.com',
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': 'DEBUG',
        'class': 'logging.StreamHandler',
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
#  Heroku settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']


STATIC_ROOT = [
    BASE_DIR / 'staticfiles'
    ]