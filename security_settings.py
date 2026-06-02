"""
Security settings to include in your Django project settings.
Import these into your my_project/settings.py:
    from hangry.security_settings import *  # noqa: F403
Or copy the relevant settings into your main settings file.
"""

import os

# SECURITY WARNING: keep the secret key used in production secret!
# Generate a new one with: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'CHANGE-ME-IN-PRODUCTION')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# HTTPS / cookie security (enable in production)
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 0 if DEBUG else 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG

# CSRF trusted origins (add your domain)
CSRF_TRUSTED_ORIGINS = os.environ.get(
    'DJANGO_CSRF_TRUSTED_ORIGINS', 'http://localhost:8000'
).split(',')

# CORS - restrict to specific origins (requires django-cors-headers)
CORS_ALLOWED_ORIGINS = os.environ.get(
    'DJANGO_CORS_ALLOWED_ORIGINS', 'http://localhost:8000'
).split(',')
CORS_ALLOW_ALL_ORIGINS = False
