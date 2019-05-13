# Generated by Django 2.1.7 on 2019-05-06 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film_session', '0001_initial'),
        ('tickets', '0006_remove_ticket_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='film_session.FilmSession'),
        ),
    ]
