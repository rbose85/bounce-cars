import os

from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """Return the value of an environment variable, or raise an exception."""
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the {} env variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# ### PROJECT

PROJECT = "bounce"
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SITE_DOMAIN = None


# ### DJANGO: https://docs.djangoproject.com/en/dev/ref/settings/

ROOT_URLCONF = "bounce.urls"


# ### DJANGO: django.conf.global_settings

TIME_ZONE = "UTC"

USE_TZ = True

LANGUAGE_CODE = "en-gb"

USE_I18N = True

USE_L10N = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2"
    }
}

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

# don't forget project apps ..
INSTALLED_APPS += (
    "bounce",
    "trades",
)

SECRET_KEY = get_env_setting("SECRET_KEY")

STATIC_ROOT = os.path.join(PROJECT_DIR, "staticfiles")
STATIC_URL = "/static/"

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)


# ### DJANGO REST FRAMEWORK: rest_framework.settings

INSTALLED_APPS += (
    "rest_framework",
)

REST_FRAMEWORK = {
    "DEFAULT_MODEL_SERIALIZER_CLASS": [
        "rest_framework.serializers.HyperlinkedModelSerializer",
    ],

    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],

    "DEFAULT_RENDERER_CLASSES": [
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],

    "DEFAULT_PARSER_CLASSES": [
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser"
    ],
}
