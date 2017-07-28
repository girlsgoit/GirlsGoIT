import environ

from .local import *

env = environ.Env()

INSTALLED_APPS += [
    'django.contrib.postgres'
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('RDS_DB_NAME'),
        'USER': env('RDS_USERNAME'),
        'PASSWORD': env('RDS_PASSWORD'),
        'HOST': env('RDS_HOSTNAME'),
        'PORT': env('RDS_PORT'),
    }
}
