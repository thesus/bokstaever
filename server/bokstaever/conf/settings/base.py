"""Settings for the bokstaever project."""

import environ
import datetime

ROOT_DIR = environ.Path(__file__) - 4
APPS_DIR = ROOT_DIR

env = environ.Env()

environ.Env.read_env(str(ROOT_DIR.path(env.str("ENVIRONMENT_FILE", ".env"))))

# Secret Key, keep this secure in production!
SECRET_KEY = env("DJANGO_SECRET_KEY")


### Application settings ###
APPLICATION_TITLE = env("DJANGO_APPLICATION_TITLE", default="bokstaever")
PAGE_SIZE = 4

### End Application settings ###


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_rq",
]

# Own applications

INSTALLED_APPS += [
    "bokstaever",
    "api",
    "dashboard",
    "frontend",
    "images",
    "django.forms",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bokstaever.urls"

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # This is used to include templates from packaged bundles
        "DIRS": [ROOT_DIR.path("bundle/templates"),],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "bokstaever.context_processors.info",
            ],
        },
    },
]

# Only use contrib as template dir in development
# The vue dashboard is served from there.
if DEBUG:
    TEMPLATES[0]["DIRS"] += ["contrib"]


WSGI_APPLICATION = "bokstaever.wsgi.application"


# Database
DATABASES = {"default": env.db("DATABASE_URL")}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation." "MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation." "CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation." "NumericPasswordValidator",},
]


# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    str(APPS_DIR.path("bundle/static/")),
    str(APPS_DIR.path("dashboard/static/"))
]

STATIC_ROOT = "static"
STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = str(APPS_DIR.path("bokstaever/media"))

LOGIN_REDIRECT_URL = "dashboard:home"
LOGIN_URL = "dashboard:login"
LOGOUT_REDIRECT_URL = "dashboard:login"

IMAGE_ROOT = env("IMAGE_ROOT", default=str(APPS_DIR.path("bokstaever/images")))

# Image configuration
IMAGE_SIZES = {"s": {"w": 400}, "m": {"w": 800}, "l": {"w": 1200}, "xl": {"w": 1800}}

# Caching
CACHES = {
    "default": env.cache("CACHE_URL", "dummycache://"),
}

# RQ
RQ_QUEUES = {
    "default": {"URL": env.str("DJANGO_REDIS_QUEUE", "redis://localhost:6379/0")}
}

APPEND_SLASH = True
