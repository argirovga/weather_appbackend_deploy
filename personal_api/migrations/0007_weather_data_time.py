# Generated by Django 3.2 on 2021-05-09 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_api', '0006_delete_clothes_recommendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather_data',
            name='time',
            field=models.TimeField(default=datetime.time(14, 10, 8, 340793)),
        ),
    ]