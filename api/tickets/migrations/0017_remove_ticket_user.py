# Generated by Django 2.1.7 on 2019-05-13 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0016_auto_20190513_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
    ]
