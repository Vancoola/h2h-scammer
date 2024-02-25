# Generated by Django 5.0.2 on 2024-02-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0045_gamemodel_away_odds_gamemodel_away_odds_old_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='away_odds',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='away_odds_old',
            field=models.FloatField(default=-1, editable=False),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='away_odds_upper',
            field=models.BooleanField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='draw_odds',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='draw_odds_old',
            field=models.FloatField(default=-1, editable=False),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='draw_odds_upper',
            field=models.BooleanField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='home_odds',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='home_odds_old',
            field=models.FloatField(default=-1, editable=False),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='home_odds_upper',
            field=models.BooleanField(default=1, editable=False),
        ),
    ]
