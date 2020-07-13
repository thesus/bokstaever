"""Settings for the bokstaever project."""

import environ
import datetime

ROOT_DIR = environ.Path(__file__) - 4
APPS_DIR = ROOT_DIR

env = environ.Env()
environ.Env.read_env(str(ROOT_DIR.path(env.str("ENVIRONMENT_FILE", ".env"))))

### Application settings ###
# Title of the application used e.g. for the rss feed
APPLICATION_TITLE = env("BOKSTAEVER_APPLICATION_TITLE", default="bokstaever")

# If the image page is enabled there is a page included that is located under `/images` including all images with `feed` == True
# On the front page there are PAGE_SIZE images injected.
INCLUDE_IMAGE_PAGE = env("BOKSTAEVER_IMAGE_PAGE", default=True)

# Images on the `/images` page if `INCLUDE_IMAGE_PATH == True`
IMAGE_PAGE_SIZE = env("BOKSTAEVER_IMAGE_PAGE_SIZE", default=16)

# Page size
PAGE_SIZE = env("BOKSTAEVER_PAGE_SIZE", default=4)
### End Application settings ###

# Secret Key, keep this secure in production!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG", default=False)

# Alowed hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_rq",
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
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bokstaever.urls"

# Form rendering is done via templates
# inputs are located in `bokstaever/templates/django/forms`
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

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
                # Include infos about the application in all templates
                "bokstaever.context_processors.info",
            ],
        },
    },
]

WSGI_APPLICATION = "bokstaever.wsgi.application"

# Database
DATABASES = {"default": env.db("DATABASE_URL")}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Internationalization
LANGUAGES = [("en", "English"), ("de", "Deutsch")]

LANGUAGE_CODE = env.str("DJANGO_LANGUAGE_CODE", "en-us")
TIME_ZONE = env.str("TIME_ZONE", "UTC")

USE_I18N = True
USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = "static"
STATIC_URL = "/static/"

# Used to include external bundle
STATICFILES_DIRS = [
    str(APPS_DIR.path("bundle/static")),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = str(APPS_DIR.path("bokstaever/media"))

# Location of the uploaded images
# At the moment they are not cleared after resizing
IMAGE_ROOT = env("IMAGE_ROOT", default=str(APPS_DIR.path("bokstaever/images")))

# Image configuration
# Note that old images are not regenerated if this changes.
IMAGE_SIZES = {"s": {"w": 400}, "m": {"w": 800}, "l": {"w": 1200}, "xl": {"w": 1800}}

# Caching
CACHES = {
    "default": env.cache("CACHE_URL", "dummycache://"),
}

# RQ
RQ_QUEUES = {
    "default": {"URL": env.str("DJANGO_REDIS_QUEUE", "redis://localhost:6379/0")}
}

# Login redirection for the dashboard
LOGIN_REDIRECT_URL = "dashboard:home"
LOGIN_URL = "dashboard:login"
LOGOUT_REDIRECT_URL = "dashboard:login"
