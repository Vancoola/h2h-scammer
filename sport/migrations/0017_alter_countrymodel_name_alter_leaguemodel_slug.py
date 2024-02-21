# Generated by Django 5.0.2 on 2024-02-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0016_alter_countrymodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrymodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='leaguemodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Слаг'),
        ),
    ]