

INSTALLED_APPS = [
    'tareas',
]
import os
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

DATABASES= {
    "default":{
        'ENGINE': "django.db.backends.mysql",
        'NAME': "tareas_db",
        'USER': "root",
        'PASSWORD': "",
        'HOST': "localhost",
        'PORT': "3306"
    
    }
}