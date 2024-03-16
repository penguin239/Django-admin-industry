"""
Django settings for django_simple project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6h6fk8sixt!!*j!)zruwg66yt$qr&asmh$_4wt0ocgw0ag*7x#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'industry.apps.IndustryConfig'
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

ROOT_URLCONF = 'django_simple.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.site_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'django_simple.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_simple',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 3307
    }
}

REDIS_CONFIG = {
    'host': '42.193.96.127',
    'port': 6379,
    'db': 0,
    'password': '$FlyPenguin6688'
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# DEBUG=False时，静态资源使用如下目录
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_TITLE = '工业管理系统'
SIMPLEUI_ANALYSIS = True
# SIMPLEUI_HOME_QUICK = False
SIMPLEUI_LOGO = 'http://42.193.96.127/static/images/default_avatar.png'

SIMPLEUI_CONFIG = {
    'system_keep': False,
    'dynamic': False,
    'menus': [
        {
            'name': '站点管理',
            'icon': 'fa-solid fa-star',
            'url': '/admin/site-manage/'
        },
        {
            'app': 'industry',
            'name': '产品管理',
            'icon': 'fa-solid fa-bars',
            'models': [
                {
                    'name': '产品列表',
                    'url': 'industry/product/'
                },
                {
                    'name': '产品类别',
                    'url': 'industry/category/'
                }
            ]
        },
        {
            'app': 'industry',
            'name': '数据库管理',
            'icon': 'fa fa-th-list',
            # 'url': 'industry/userinfo', # 直接显示
            'models': [
                {
                    'name': '员工数据库',
                    'url': 'industry/userinfo/',
                    'icon': 'fa fa-user'
                },
                {
                    'name': '货物数据库',
                    'url': 'industry/userinfo/',
                    'icon': 'fa-solid fa-cart-shopping'
                }
            ]
        },
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                }
            ]
        },
    ]
}
