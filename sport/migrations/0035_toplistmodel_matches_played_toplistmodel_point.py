# Generated by Django 5.0.2 on 2024-02-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0034_rename_lost_toplistmodel_lose'),
    ]

    operations = [
        migrations.AddField(
            model_name='toplistmodel',
            name='matches_played',
            field=models.IntegerField(default=0, verbose_name='Матчей сыграно'),
        ),
        migrations.AddField(
            model_name='toplistmodel',
            name='point',
            field=models.IntegerField(default=0, verbose_name='Очков'),
        ),
    ]