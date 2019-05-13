import uuid

from django.db import models

from ..users.models import User
from ..film_session.models import FilmSession


class Ticket(models.Model):
    session = models.ForeignKey(FilmSession,
                                on_delete=models.CASCADE,
                                null=True
                                )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             related_name='tickets')

    ticket_number = models.UUIDField(primary_key=True,
                                     default=uuid.uuid1)

    row_number = models.IntegerField(blank=True,
                                     null=True)
    seat_number = models.IntegerField(blank=True,
                                      null=True)

    time_reserv = models.TimeField(null=True)

    price = models.IntegerField(blank=True,
                                null=True)

    free_place = models.BooleanField(default=True)

    class Meta:
        ordering = ['session']
        db_table = 'tickets'



