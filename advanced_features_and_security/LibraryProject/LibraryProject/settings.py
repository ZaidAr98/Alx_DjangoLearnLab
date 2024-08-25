"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6+8h*0(9*d&zkhcm!bs)y(rtq7nw332po=y94575yx^3)f(s-z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': '273879',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }

}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/'


AUTH_USER_MODEL = 'bookshelf.CustomUser'

DEBUG = False


ALLOWED_HOSTS = ['http://127.0.0.1:3000']


SECURE_BROWSER_XSS_FILTER = True  # Enables the X-XSS-Protection header in HTTP responses.
X_FRAME_OPTIONS = 'DENY'  # Prevents the site from being framed (clickjacking protection).
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents the browser from trying to guess the content type.

# Secure cookies:
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are only sent over HTTPS.
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS.



# Example CSP configuration:
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'https://stackpath.bootstrapcdn.com')
CSP_SCRIPT_SRC = ("'self'", 'https://code.jquery.com')




# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# Use HTTP Strict Transport Security (HSTS) to force browsers to communicate with the site only over HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow preloading of the HSTS policy in supported browsers

# Security-related Headers
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking by not allowing the site to be framed
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from guessing the content type
SECURE_BROWSER_XSS_FILTER = True  # Enable the browser’s XSS filtering



# Secure cookies settings
SESSION_COOKIE_SECURE = True  # Ensure session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are only sent over HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
