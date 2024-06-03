# Generated by Django 5.0.6 on 2024-06-03 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(max_length=1000, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MacAddress',
            fields=[
                ('id', models.AutoField(max_length=10000, primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=250)),
                ('id_user', models.ForeignKey(max_length=10000, on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]
