import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'tareas',
    'rest_framework',
    'rest_framework_swagger',
    'drf_yasg',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

DATABASES = {
    "default": {
        'ENGINE': "django.db.backends.mysql",
        'NAME': "tareas_db",
        'USER': "root",
        'PASSWORD': "",
        'HOST': "localhost",
        'PORT': "3306",
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES',
        },
    }
}
