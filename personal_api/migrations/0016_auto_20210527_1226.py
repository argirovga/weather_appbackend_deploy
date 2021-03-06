# Generated by Django 3.2.2 on 2021-05-27 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_api', '0015_auto_20210512_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather_data',
            name='feels_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='humidity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='pressure',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='temp_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='temp_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='time',
            field=models.TimeField(default=datetime.time(12, 26, 9, 685172)),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='wind_speed',
            field=models.IntegerField(default=0),
        ),
    ]
