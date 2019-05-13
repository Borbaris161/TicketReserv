import datetime

from rest_framework import serializers
from .models import Ticket
from ..users.models import User


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                              many=False,
                                              required=False
                                              )

    def update(self, ticket, data):
        if not ticket.user:
            ticket.user = data['user']
            ticket.free_place = False
            ticket.time_reserv = datetime.datetime.now().time()
            ticket.save()
        return ticket

    class Meta:
        model = Ticket
        ordering = ['price']
        fields = (
            'row_number',
            'seat_number',
            'user'
        )

