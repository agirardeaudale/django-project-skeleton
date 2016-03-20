"""Development settings and globals."""

from os.path import join
from {{ project_name }}.settings.common import *


###########################################################
# DEBUG CONFIGURATION
DEBUG = True


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
INSTALLED_APPS = DEFAULT_APPS
