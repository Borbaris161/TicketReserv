from django.db import models


class Hall(models.Model):
    title = models.CharField(primary_key=True, max_length=30, default=None)
    rows = models.IntegerField(null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        db_table = 'hall'





