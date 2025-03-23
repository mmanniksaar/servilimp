import os
from pathlib import Path
import dj_database_url
#import redis
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')

#DEBUG = os.environ.get('DEBUG', 'False') == 'True'
DEBUG = True #False

ALLOWED_HOSTS = ['servilimp.fi', 'www.servilimp.fi', '127.0.0.1', 'localhost', 'servilimp-16a386567b31.herokuapp.com', 'www.servilimp-16a386567b31.herokuapp.com']


INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
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
    'apps.about',
    'apps.accounts',
    'apps.carts',
    'cloudinary',
    'crispy_forms',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'meta',
    #'sslserver',

    #'axes',
    #'defender',
]

""" # Suunab kõik HTTP-päringud automaatselt HTTPS-ile
SECURE_SSL_REDIRECT = True   # Tootmisversioonis peab olema True

SECURE_HSTS_SECONDS = 31536000  
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  
SECURE_HSTS_PRELOAD = True  

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

if DEBUG:
# Suunab kõik HTTP-päringud automaatselt HTTPS-ile
    SECURE_SSL_REDIRECT = False  # Tootmisversioonis peab olema True
# Tagab, et sessiooni ja CSRF küpsised saadetakse ainult HTTPS kaudu
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    # HSTS seaded võivad samuti olla arenduskeskkonnas välja lülitatud
    SECURE_HSTS_SECONDS = 0
else:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # HSTS seaded
    SECURE_HSTS_SECONDS = 31536000          # 1 aasta (sekundites)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True   # Ka alamdomeenide jaoks
    SECURE_HSTS_PRELOAD = True              # Kui soovid end registreerida preload nimekirjadesse

 """

SITE_ID = 1

META_SITE_PROTOCOL = "https"
META_SITE_DOMAIN = "www.servilimp.fi"
LOGIN_REDIRECT_URL = '/cart/merge_cart/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    #'defender.middleware.FailedLoginMiddleware',
    #'axes.middleware.AxesMiddleware',
]

AUTH_USER_MODEL = 'accounts.Account'


ROOT_URLCONF = 'project_Servilimp.urls'

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = (
    "'self'",
    "https://trusted.cdn.com",
    "https://cdnjs.cloudflare.com",
)
CSP_STYLE_SRC = (
    "'self'",
    "https://trusted.cdn.com",
    "https://cdnjs.cloudflare.com",
)
CSP_IMG_SRC = ("'self'", "https://res.cloudinary.com", "data:")
CSP_FONT_SRC = (
    "'self'",
    "https://cdnjs.cloudflare.com",
)

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
                'apps.carts.context_processors.counter', #now context_processors is available in all templates

            ],
        },
    },
]

WSGI_APPLICATION = 'project_Servilimp.wsgi.application'

DJANGO_CHECK_SEO_SETTINGS = {
    "content_words_number": [300, 600],
    "internal_links": 1,
    "external_links": 1,
    "meta_title_length": [30, 60],
    "meta_description_length": [50, 160],
    "keywords_in_first_words": 50,
    "max_link_depth": 3,
    "max_url_length": 70,
}


# if os.environ.get('DJANGO_ENV') == 'production':
#     REDIS_URL = os.environ.get('REDISCLOUD_URL_REMOTE')
# else:
#     REDIS_URL = os.environ.get('REDISCLOUD_URL_LOCAL')

# redis_url = urlparse(REDIS_URL) if REDIS_URL else None

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': '',
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }

# if redis_url:
#     CACHES['default'] = {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': f"redis://{redis_url.hostname}:{redis_url.port}/0",
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'PASSWORD': redis_url.password,
#             'SOCKET_CONNECT_TIMEOUT': 5,  # in seconds
#             'SOCKET_TIMEOUT': 5,  # in seconds
#         }
#     }

#AXES_REDIS_URL = f"{REDIS_URL}/1" if REDIS_URL else None
#DEFENDER_REDIS_URL = f"{REDIS_URL}/2" if REDIS_URL else None


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

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#AXES_REDIS_URL = os.getenv('REDISCLOUD_URL') + '/1'
#DEFENDER_REDIS_URL = os.getenv('REDISCLOUD_URL') + '/2'



# AUTHENTICATION_BACKENDS = [
#      'axes.backends.AxesStandaloneBackend',
#      'django.contrib.auth.backends.ModelBackend',
#  ]

# AXES_ENABLED = True
# AXES_FAILURE_LIMIT = 3
# AXES_COOLOFF_TIME = 10
# AXES_VERBOSE = True
# AXES_LOCK_OUT_BY_USER_AND_IP = False
# AXES_IP_WHITELIST = '127.0.0.1'

#AXES_LOCKOUT_TEMPLATE = 'axes/lockout.html'


#DEFENDER_LOGIN_FAILURE_LIMIT = 10
#DEFENDER_COOLOFF_TIME = 0  # 3 minutes
#DEFENDER_DISABLE_IP_LOCKOUT = False
#DEFENDER_DISABLE_USERNAME_LOCKOUT = False
#DEFENDER_LOCKOUT_TEMPLATE = 'path/to/lockout_template.html'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
STATICFILES_DIRS = [
    'static',
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_MANIFEST_STRICT = False


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
    DATABASES = {'default': dj_database_url.config(conn_max_age=600)}
else:
    # Lokaliseerimiseks (local development) kasutame SQLite'i.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            'CONN_MAX_AGE': 60,
        }
    }



