from django.db import models


class Film(models.Model):
    title = models.CharField(primary_key=True, max_length=30, default=None)
    duration = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        db_table = 'films'