# Generated by Django 3.2.2 on 2021-05-12 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_api', '0012_alter_weather_data_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_preferences',
            name='fall_out_pref',
        ),
        migrations.RemoveField(
            model_name='user_preferences',
            name='user',
        ),
        migrations.AddField(
            model_name='user_preferences',
            name='humidity_pref',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_preferences',
            name='name',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='user_preferences',
            name='user_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='user_preferences',
            name='temp_pref',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_preferences',
            name='wind_pref',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='time',
            field=models.TimeField(default=datetime.time(15, 41, 22, 189377)),
        ),
    ]
