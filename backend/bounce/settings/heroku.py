import dj_database_url

from .base import *


#### PROJECT

PROJECT += '-heroku'
SITE_DOMAIN = 'desolate-bastion-6667.herokuapp.com'


#### DJANGO

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [SITE_DOMAIN, ]


#### DJANGO: django.conf.global_settings

DATABASES['default'] = dj_database_url.config()

INSTALLED_APPS += (
    'gunicorn',
)

WSGI_APPLICATION = 'heroku.wsgi.heroku.application'

MIDDLEWARE_CLASSES = ('sslify.middleware.SSLifyMiddleware', ) + MIDDLEWARE_CLASSES

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s [%(name)s:%(lineno)s] %(message)s'
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },

    'loggers': {

        #### D J A N G O ####
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },

        #### P R O J E C T ####
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_DOMAIN = SITE_DOMAIN
CSRF_COOKIE_SECURE = True


#### HEROKU

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
