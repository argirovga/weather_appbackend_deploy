# Generated by Django 3.1.4 on 2021-03-02 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wether_data',
            name='main_description',
        ),
    ]
