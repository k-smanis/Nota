from .base import BASE_DIR
import os
from dotenv import dotenv_values

# Load Dev Environment Variables
dev_env_values = dotenv_values(".env")

# Secret Key
SECRET_KEY = dev_env_values["DEBUG_SECRET_KEY"]
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set. Fix your environment.")

# Allowed Hosts
allowed_hosts_raw = dev_env_values.get("DEBUG_ALLOWED_HOSTS", "")
if not allowed_hosts_raw:
    raise ValueError("DEBUG_ALLOWED_HOSTS is not set. Fix your environment.")
ALLOWED_HOSTS = allowed_hosts_raw.split(",")

# Database (https://docs.djangoproject.com/en/5.1/ref/settings/#databases)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
