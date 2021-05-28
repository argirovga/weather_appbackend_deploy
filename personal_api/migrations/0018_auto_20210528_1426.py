# Generated by Django 3.2.2 on 2021-05-28 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_api', '0017_auto_20210527_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_preferences',
            name='last_hum',
            field=models.IntegerField(default=-100),
        ),
        migrations.AlterField(
            model_name='user_preferences',
            name='last_temp',
            field=models.IntegerField(default=-100),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='time',
            field=models.TimeField(default=datetime.time(14, 26, 45, 344265)),
        ),
    ]