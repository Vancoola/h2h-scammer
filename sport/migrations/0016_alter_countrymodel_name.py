# Generated by Django 5.0.2 on 2024-02-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0015_rename_code_country_countrymodel_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrymodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
    ]
