import datetime

from rest_framework import serializers

from .models import FilmSession
from ..films.models import Film
from ..halls.models import Hall
from ..tickets.models import Ticket
from ..tickets.serializers import TicketSerializer


def create_tickets(session, ticket_data):
    rows = session.hall.rows
    seats = session.hall.seats
    for row in range(1, rows + 1):
        for seat in range(1, seats + 1):
            Ticket.objects.create(row_number=row,
                                  seat_number=seat,
                                  session=session,
                                  **ticket_data
                                  )


class FilmSessionSerializer(serializers.ModelSerializer):
    hall = serializers.PrimaryKeyRelatedField(
        queryset=Hall.objects.all(), read_only=False, required=False)

    film = serializers.PrimaryKeyRelatedField(
        queryset=Film.objects.all(), read_only=False, required=False)

    ticket = TicketSerializer(read_only=False, many=False, required=False)

    advertising_duration = 10
    cleaning_duration = 15
    first_session = datetime.time(8, 0, 0)
    last_session = datetime.time(23, 0, 0)

    def create(self, validated_data):
        ticket_data = validated_data.pop('ticket')
        session = FilmSession.objects.create(**validated_data)
        create_tickets(session, ticket_data)
        return session

    def validate(self, data):
        film_data = data['film']
        beginning_session = data['beginning_session']
        if self.last_session >= beginning_session >= self.first_session:
            session_duration = datetime.timedelta(
                minutes=film_data.duration +
                        self.advertising_duration +
                        self.cleaning_duration
            )
            session_end = (datetime.datetime.strptime(str(beginning_session),
                                                      "%H:%M:%S") +
                           session_duration).time()
            data['ending_session'] = session_end
            if FilmSession.objects.exists():
                current_film = FilmSession.objects.order_by('beginning_session')
                for film in current_film:
                    if film.beginning_session < beginning_session < film.ending_session:
                        raise serializers.ValidationError("This session time is already exist for %s" % film.film_id)
                    else:
                        return data
            else:
                return data
        else:
            raise serializers.ValidationError("This session time not available")

    class Meta:
        model = FilmSession
        fields = (
            'beginning_session',
            'ticket',
            'hall',
            'film',
            )