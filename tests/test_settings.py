DEBUG = False

SECRET_KEY = "not-secret"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "LOCATION": ":memory:"}
}

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = []

MIDDLEWARE = (
    'django_floc_disable.middleware.FLoCDisableMiddleware',
)

ROOT_URLCONF = "tests.test_urls"

STATIC_URL = "/static/"

TEMPLATES = []
