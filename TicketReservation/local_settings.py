DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cinema_db',
        'USER': 'borbaris161',
        'PASSWORD': '12345',
        'HOST': 'db',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_cinema',
        },
    }
}

