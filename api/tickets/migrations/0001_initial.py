# Generated by Django 2.1.7 on 2019-05-06 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('film_session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_number', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('row_number', models.IntegerField(blank=True, null=True)),
                ('seat_number', models.IntegerField(blank=True, null=True)),
                ('places_number', models.IntegerField(null=True)),
                ('time_reserv', models.TimeField(null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('free_place', models.BooleanField(default=True, verbose_name='status')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='film_session.FilmSession')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
    ]
