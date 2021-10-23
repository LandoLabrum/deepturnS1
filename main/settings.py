import environ
import os

env = environ.Env()
environ.Env.read_env()  

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'account',
    'lead',
    'form',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'django_better_admin_arrayfield',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'DIRS': [BASE_DIR + "/templates", ],
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

WSGI_APPLICATION = 'main.wsgi.application'




DATABASES = {'default': env.db('DATABASE_URL')}




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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# AWS S3 CONFIG
# AWS_ACCESS_KEY_ID=env.str('S3_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY=env.str('S3_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME=env.str('S3_STORAGE_BUCKET_NAME')

# AWS_S3_FILE_OVERWRITE=False
# AWS_DEFAULT_ACL=None
# DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'