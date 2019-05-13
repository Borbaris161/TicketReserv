from django.conf.urls import url
from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView, UserData

urlpatterns = [
    url(r'^api/v0/registration/$', CreateUserAPIView.as_view()),
    url(r'^api/v0/authenticate_user/$', authenticate_user),
    url(r'^api/v0/update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^api/v0/lk/my-tickets/$', UserData.as_view()),
]
