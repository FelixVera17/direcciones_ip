# Generated by Django 5.0.6 on 2024-06-05 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_macaddress_date_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macaddress',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 16, 22, 54, 150878, tzinfo=datetime.timezone.utc)),
        ),
    ]
