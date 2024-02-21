# Generated by Django 5.0.2 on 2024-02-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0031_teammodel_league_alter_toplistmodel_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='game_id',
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
        migrations.AlterUniqueTogether(
            name='toplistmodel',
            unique_together={('league', 'team')},
        ),
    ]