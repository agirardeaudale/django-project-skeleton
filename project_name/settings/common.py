"""Common settings and globals."""

import sys
from os.path import abspath, basename, dirname, join, normpath


###########################################################
# DEBUG CONFIGURATION

DEBUG = False


###########################################################
# PATH CONFIGURATION

# Fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# The name of the whole site
SITE_NAME = basename(DJANGO_ROOT)

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
]

# Add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))


###########################################################
# STATIC FILE CONFIGURATION

# Collect static files here
STATIC_ROOT = join(PROJECT_ROOT, 'run', 'static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# look for static assets here
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'static'),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


###########################################################
# MEDIA CONFIGURATION

# Collect media files here
MEDIA_ROOT = join(PROJECT_ROOT, 'run', 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


###########################################################
# FIXTURE CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(PROJECT_ROOT, 'fixtures')),
)


###########################################################
# DJANGO RUNNING CONFIGURATION

# The default WSGI application
WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)

# The root URL configuration
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)

# This site's ID
SITE_ID = 1


###########################################################
# INTERNATIONALIZATION

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'

# Internationalization
USE_I18N = True

# Localisation
USE_L10N = True

# Timezone awareness
USE_TZ = True


###########################################################
# APPLICATION CONFIGURATION

# Apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # Asynchronous task queue:
    'djcelery',

    # Static file management:
    'compressor',
]

LOCAL_APPS = [
]

COMMON_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Jinja2 templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': '{}.jinja2.environment'.format(SITE_NAME)[,
        },
    },
]


###########################################################
# CELERY CONFIGURATION

# See: http://celery.readthedocs.org/en/latest/configuration.html#celery-task-result-expires
CELERY_TASK_RESULT_EXPIRES = timedelta(minutes=30)

# See: http://docs.celeryproject.org/en/master/configuration.html#std:setting-CELERY_CHORD_PROPAGATES
CELERY_CHORD_PROPAGATES = True

# See: http://celery.github.com/celery/django/
setup_loader()


###########################################################
# COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED
COMPRESS_ENABLED = True

# See: http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_HASHING_METHOD
COMPRESS_CSS_HASHING_METHOD = 'content'

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]


###########################################################
# SECURITY/ADMIN/SECRET CONFIGURATION

# We store the secret key here
SECRET_FILE = normpath(join(PROJECT_ROOT, 'run', 'SECRET.key'))

# These persons receive error notification
ADMINS = (
    ('Andrew Girardeau-Dale', 'agirardeaudale@gmail.com'),
)
MANAGERS = ADMINS

try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
        SECRET_KEY = get_random_string(50, chars)
        with open(SECRET_FILE, 'w') as f:
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Could not open %s for writing!' % SECRET_FILE)
