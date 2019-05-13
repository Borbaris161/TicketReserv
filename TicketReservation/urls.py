from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^user/', include('api.users.urls')),
    url(r'^films/', include('api.films.urls')),
    url(r'^film_session/', include('api.film_session.urls')),
    url(r'^tickets/', include('api.tickets.urls')),
]
