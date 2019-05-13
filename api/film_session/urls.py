from django.conf.urls import url
from .views import CreateSessionAPIView, SessionList

urlpatterns = [
    url(r'^api/v0/create/$', CreateSessionAPIView.as_view()),
    url(r'^api/v0/all/$', SessionList.as_view()),
]
