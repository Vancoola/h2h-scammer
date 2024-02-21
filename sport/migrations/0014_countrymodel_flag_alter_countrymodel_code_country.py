# Generated by Django 5.0.2 on 2024-02-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0013_alter_columnmodel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrymodel',
            name='flag',
            field=models.URLField(blank=True, null=True, verbose_name='Флаг'),
        ),
        migrations.AlterField(
            model_name='countrymodel',
            name='code_country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код'),
        ),
    ]
