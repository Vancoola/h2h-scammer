# Generated by Django 5.0.2 on 2024-02-19 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0027_infomodel_country_alter_infomodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infomodel',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.countrymodel'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='facebook',
            field=models.CharField(max_length=255, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='instagram',
            field=models.CharField(max_length=255, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='telegram',
            field=models.CharField(max_length=255, verbose_name='Телеграм'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='telenumber',
            field=models.CharField(max_length=255, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='whatsup',
            field=models.CharField(max_length=255, verbose_name='WhatsUp'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='x',
            field=models.CharField(max_length=255, verbose_name='X'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='youtube',
            field=models.CharField(max_length=255, verbose_name='YouTube'),
        ),
    ]