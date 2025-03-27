from .base import BASE_DIR

# Secret Key
SECRET_KEY = ""  # TODO: Add production SECRET_KEY before deployment
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set. Fix your environment.")

# Allowed Hosts
ALLOWED_HOSTS = []  # TODO: Add production ALLOWED_HOSTS before deployment

# Database (https://docs.djangoproject.com/en/5.1/ref/settings/#databases)
DATABASES = {  # TODO: Add production DATABASES before deployment
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

#
SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
