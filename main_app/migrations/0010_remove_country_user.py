# Generated by Django 4.1.2 on 2022-10-07 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_country_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='user',
        ),
    ]
