# Generated by Django 2.1.7 on 2019-05-07 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film_session', '0003_auto_20190507_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmsession',
            name='ticket',
            field=models.OneToOneField(auto_created=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_price', to='tickets.Ticket'),
        ),
    ]
