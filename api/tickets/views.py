from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import serializers
from rest_framework import \
    (status, generics, )

from rest_framework.permissions import \
    (IsAuthenticated,)

from .serializers import TicketSerializer
from .models import Ticket


class CreateReservAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all().filter(free_place=True)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(session=self.request.data['session'],
                           row_number=self.request.data['row'],
                           seat_number=self.request.data['seat'])
        return obj

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        ticket_data = request.data
        ticket_data['user'] = request.user.id
        ticket = self.get_object()
        serializer = TicketSerializer(ticket, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all().filter(free_place=True)
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TicketView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def list(self, request):
        queryset = Ticket.objects.filter(user_id=request.user.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
