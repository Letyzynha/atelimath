"""
Configurações de Produção para o projeto AteliMatch.
"""
from .base import *
from decouple import config
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

# Database
# Configuração para PostgreSQL (Neon/ElephantSQL)
DATABASE_URL = config('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}

# Configurações de Segurança
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# Outras configurações de segurança...

# Configuração de Logs para Produção
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

# Note: dj-database-url já está no requirements.txt
