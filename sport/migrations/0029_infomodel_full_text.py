# Generated by Django 5.0.2 on 2024-02-19 17:09

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0028_alter_infomodel_country_alter_infomodel_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomodel',
            name='full_text',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='SEO Текст'),
        ),
    ]