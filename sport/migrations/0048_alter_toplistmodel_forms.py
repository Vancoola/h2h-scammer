# Generated by Django 5.0.2 on 2024-02-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0047_toplistmodel_forms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toplistmodel',
            name='forms',
            field=models.CharField(default='', max_length=6),
        ),
    ]
