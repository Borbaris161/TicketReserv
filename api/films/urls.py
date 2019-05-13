from django.conf.urls import url
from .views import create_film, FilmList

urlpatterns = [
    url(r'^api/v0/create/$', create_film),
    url(r'^api/v0/all/$', FilmList.as_view()),
]
