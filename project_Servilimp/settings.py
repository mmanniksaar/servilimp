import os
from pathlib import Path
import dj_database_url
import redis
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['www.servilimp.fi', '127.0.0.1','servilimp-3a5ad048a799.herokuapp.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'apps.gallery',
    'apps.clients',
    'apps.rental',
    'apps.category',
    'cloudinary',
    'crispy_forms',
    'axes',
    'defender',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'defender.middleware.FailedLoginMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'project_Servilimp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.category.context_processors.menu_links', #now context_processors is available in all templates
            ],
        },
    },
]

WSGI_APPLICATION = 'project_Servilimp.wsgi.application'


redis_url = urlparse(os.environ.get('REDISCLOUD_URL'))

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{redis_url.hostname}:{redis_url.port}/1',
        'OPTIONS': {
            'PASSWORD': redis_url.password,
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Heroku provides Redis URL in REDISCLOUD_URL environment variable
#REDIS_URL = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379/0')
#redis_instance = redis.from_url(REDIS_URL)


#AXES_REDIS_URL = os.getenv('REDISCLOUD_URL') + '/1'
#DEFENDER_REDIS_URL = os.getenv('REDISCLOUD_URL') + '/2'



AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]


DEFENDER_LOGIN_FAILURE_LIMIT = 3
DEFENDER_COOLOFF_TIME = 180  # 3 minutes
#DEFENDER_LOCKOUT_TEMPLATE = 'path/to/lockout_template.html'


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'project_Servilimp/static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#media files conf
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

EMAIL_HOST = os.environ.get('EMAIL_HOST_NAME')
EMAIL_PORT = os.environ.get('EMAIL_PORT_NUMBER')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PWD')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS_STATE')


if 'DATABASE_URL' in os.environ:
    DATABASES = {'default': dj_database_url.config()}
else:
    # Lokaliseerimiseks (local development) kasutame SQLite'i.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }