# Generated by Django 5.0.2 on 2024-02-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0035_toplistmodel_matches_played_toplistmodel_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='toplistmodel',
            name='is_away',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='toplistmodel',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
