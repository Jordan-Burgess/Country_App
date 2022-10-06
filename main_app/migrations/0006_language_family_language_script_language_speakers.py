# Generated by Django 4.1.2 on 2022-10-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='family',
            field=models.CharField(default='Apple', max_length=150),
        ),
        migrations.AddField(
            model_name='language',
            name='script',
            field=models.CharField(default='Apple', max_length=150),
        ),
        migrations.AddField(
            model_name='language',
            name='speakers',
            field=models.IntegerField(default=1),
        ),
    ]
