from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOWED_ORIGINS = [
#     'https://whaling.co.kr',
#     'https://*.whaling.co.kr',
#     'http://localhost:3000',
#     'http://127.0.0.1:8000',
# ]
# CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [
    'https://whaling.co.kr',
    'https://*.whaling.co.kr',
]
