from .base import *

DEBUG = False

try:
    from base import *
except ImportError:
    pass

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['stupid-frickin-website.fly.dev']
CSRF_TRUSTED_ORIGINS = ['stupid-frickin-website.fly.dev']
