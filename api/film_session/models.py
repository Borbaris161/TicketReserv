import datetime
from django.db import models

from ..halls.models import Hall
from ..films.models import Film


class FilmSession(models.Model):
    hall = models.ForeignKey(
        Hall,
        related_name='halls',
        on_delete=models.CASCADE,
        null=True
    )

    film = models.ForeignKey(
        Film,
        related_name='films',
        on_delete=models.CASCADE,
        null=True
    )

    beginning_session = models.TimeField(primary_key=True, blank=True, default=None)
    ending_session = models.TimeField(default=None, blank=False, null=True)

    beginnig_sessions = datetime.time(8, 0, 0)
    ending_sessions = datetime.time(23, 0, 0)

    class Meta:
        ordering = ['beginning_session']
        db_table = 'film_session'

    def __str__(self):
        return str(self.beginning_session)
