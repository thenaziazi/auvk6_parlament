import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')


DEBUG = os.getenv('DEBUG','False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS','localhost').split(',')


MY_APPS = [
    'apps.events',
    'apps.ministries',
    'apps.tasks',
    'apps.users',
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.getenv('SUPABASE_DB_PASSWORD'),
        'HOST': os.getenv('SUPABASE_DB_HOST'),
        'PORT': '5432',
    }
}



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




LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


AUTH_USER_MODEL = 'users.CustomUser'


JAZZMIN_SETTINGS = {
    "site_title": "Парламент",
    "site_header": "Парламент",
    "site_brand": "АУВК Парламент",
    "welcome_sign": "Панель управления",
    "copyright": "АУВК Парламент",
    "site_logo":  'logo.jpg',
    "site_icon": None,

    "welcome_sign": "Welcome to the library",

    # Copyright on the footer
    "copyright": "Acme Library Ltd",

    "search_model": ["auth.User", "auth.Group"],

    "user_avatar": None,

    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "events"},
        {"app": "tasks"},
        {"app": "ministries"},
        {"app": "users"},
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "users.CustomUser": "fas fa-user-tie",
        "ministries.Ministries": "fas fa-landmark",
        "ministries.MinistryGoals": "fas fa-bullseye",
        "tasks.Tasks": "fas fa-tasks",
        "events.Events": "fas fa-calendar-check",
        "events.EventsToOrganize": "fas fa-calendar-plus",
        "events.YearPlan": "fas fa-calendar-alt",
    },

 

    "usermenu_links": [
        {"model": "auth.user"}
    ],


    "order_with_respect_to": [
        "events",
        "tasks", 
        "ministries",
        "users",
        "auth",
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}