DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'api_cinema_db',
        'USER': 'borbaris161',
        'PASSWORD': 'qwerfvbnm',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_cinema',
        },
    }
}

