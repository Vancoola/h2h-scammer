# Generated by Django 5.0.2 on 2024-02-14 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0006_remove_gamemodel_slug_leaguemodel_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(blank=True, null=True, verbose_name='Место')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='league', to='sport.leaguemodel')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='sport.teammodel')),
            ],
        ),
    ]
