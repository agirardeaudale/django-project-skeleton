"""Development settings and globals."""

from os.path import join
from {{ project_name }}.settings.common import *


###########################################################
# DATABASE CONFIGURATION

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
    }
}


###########################################################
# APPLICATION CONFIGURATION

DEVELOPMENT_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS = COMMON_APPS

# MEMCACHE
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# CELERY
# See: http://docs.celeryq.org/en/latest/configuration.html#celery-always-eager
CELERY_ALWAYS_EAGER = True

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-eager-propagates-exceptions
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

# DEBUG TOOLBAR
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = [
    '127.0.0.1'
]

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
