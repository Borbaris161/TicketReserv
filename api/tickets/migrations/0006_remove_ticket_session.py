# Generated by Django 2.1.7 on 2019-05-06 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20190506_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='session',
        ),
    ]
