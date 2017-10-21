import environ
import raven
import os

BASE_DIR = environ.Path(__file__) - 2
PROJECT_ROOT = environ.Path(__file__) - 1

# Load operating system environment variables and then prepare to use them
env = environ.Env()
environ.Env.read_env(str(BASE_DIR.path('.env')))

DEBUG = env.bool('DJANGO_DEBUG', False)
SECRET_KEY = env('DJANGO_SECRET_KEY')

ROOT_URLCONF = '{{cookiecutter.project_slug}}.urls'
WSGI_APPLICATION = '{{cookiecutter.project_slug}}.wsgi.application'

# Allow all host headers
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['localhost'])

ADMINS = [
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
]
MANAGERS = ADMINS

SITE_ID = 1

# HTTPS --------------------------------------------------------------------------------------------

# Enforce HTTPS when not running in DEBUG mode
SECURE_SSL_REDIRECT = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# I18N ---------------------------------------------------------------------------------------------

LANGUAGE_CODE = env('DJANGO_LANGUAGE_CODE', default='en-us')
TIME_ZONE = env('DJANGO_TIME_ZONE', default='UTC')
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DATABASE -----------------------------------------------------------------------------------------

DATABASES = {
    'default': env.db('DATABASE_URL', default='mysql://root@localhost/{{cookiecutter.project_slug}}')
}

# I prefer to tie my transactions to HTTP requests
# https://docs.djangoproject.com/en/1.11/topics/db/transactions/#tying-transactions-to-http-requests
DATABASES['default']['ATOMIC_REQUESTS'] = True

# performance tweak and hint for heroku
DATABASES['default']['CONN_MAX_AGE'] = 500

# Activating 'read committed' as the default isolation level. Django 2.0 will do this anyway.
DATABASES['default']['OPTIONS'] = {}
DATABASES['default']['OPTIONS']['isolation_level'] = 'read committed'

# APPS ---------------------------------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'compressor',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    '{{cookiecutter.project_slug}}.apps.users',
]

# MIDDLEWARES --------------------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# PASSWORD VALIDATION ------------------------------------------------------------------------------

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

# AUTHENTICATION -----------------------------------------------------------------------------------

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_ADAPTER = '{{cookiecutter.project_slug}}.apps.users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = '{{cookiecutter.project_slug}}.apps.users.adapters.SocialAccountAdapter'

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

# PASSWORD -----------------------------------------------------------------------------------------

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# COMPRESSOR AND LIBSASS ---------------------------------------------------------------------------

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
LIBSASS_SOURCEMAPS = True
LIBSASS_PRECISION = 8

# STATIC FILE SERVING ------------------------------------------------------------------------------

STATIC_ROOT = str(BASE_DIR.path('staticfiles'))
STATIC_HOST = env('DJANGO_STATIC_HOST', default='')
STATIC_URL = STATIC_HOST + '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    str(PROJECT_ROOT.path('static')),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# SLUGLIFIER ---------------------------------------------------------------------------------------

AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# TEMPLATES ----------------------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(PROJECT_ROOT.path('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

# LOGGING ------------------------------------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': env('DJANGO_LOG_LEVEL', default='INFO'),
        }
    }
}

# SENTRY -------------------------------------------------------------------------------------------

RAVEN_DSN = env('RAVEN_DSN', default=None)

if RAVEN_DSN:
    INSTALLED_APPS += [
        'raven.contrib.django.raven_compat',
    ]

    RAVEN_CONFIG = {
        'dsn': RAVEN_DSN,
        'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
    }

# DJANGO DEBUG TOOLBAR -----------------------------------------------------------------------------

if DEBUG:
    ALLOWED_HOSTS += ['127.0.0.1']
    INTERNAL_IPS = ('127.0.0.1', 'localhost',)
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
    }
