# Generated by Django 5.0.2 on 2024-02-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0036_toplistmodel_is_away_toplistmodel_is_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='toplistmodel',
            name='goalsDiff',
            field=models.IntegerField(default=0, verbose_name='GD'),
        ),
    ]
