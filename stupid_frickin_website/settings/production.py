from .base import *
import environ
env = environ.Env()

try:
    from base import *
except ImportError:
    pass

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=['stupid.frickin.website', ])
CSRF_TRUSTED_ORIGINS = ['https://' + host for host in ALLOWED_HOSTS]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env('SQLITE3_PATH', default='/db/db.sqlite3'),
    }
}

STATIC_ROOT = env('STATIC_ROOT', default='/static')

MEDIA_ROOT = env('MEDIA_ROOT', default='/media')
MEDIA_URL = '/media/'

sentry_sdk.init(
    dsn=env('SENTRY_DSN', default=None),
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
