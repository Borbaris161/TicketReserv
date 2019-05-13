from django.conf.urls import url
from .views import TicketList, CreateReservAPIView, TicketView

urlpatterns = [
    url(r'^api/v0/sessions/$', TicketList.as_view()),
    url(r'^api/v0/reserv/$', CreateReservAPIView.as_view()),
    url(r'^api/v0/ticket_data/$', TicketView.as_view())

]
