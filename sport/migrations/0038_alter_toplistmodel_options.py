# Generated by Django 5.0.2 on 2024-02-21 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0037_toplistmodel_goalsdiff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toplistmodel',
            options={'ordering': ('point',)},
        ),
    ]
