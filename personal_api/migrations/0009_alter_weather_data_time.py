# Generated by Django 3.2 on 2021-05-09 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_api', '0008_alter_weather_data_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather_data',
            name='time',
            field=models.TimeField(default=datetime.time(14, 11, 15, 673898)),
        ),
    ]
