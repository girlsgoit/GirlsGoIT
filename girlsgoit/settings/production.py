from .local import *

env = os.environ.get

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

ALLOWED_HOSTS = [
    'girlsgoitplatform-env.g2ku3zr4a4.eu-west-1.elasticbeanstalk.com',
    'moldova.girlsgoit.org',
]
