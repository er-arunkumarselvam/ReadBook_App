# Generated by Django 4.2.5 on 2023-09-17 14:10

import ReadBookApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReadBookApp', '0006_alter_bookproduct_booklanguage_alter_genre_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookproduct',
            name='bookLanguage',
            field=models.CharField(choices=[('Tamil', 'TAMIL'), ('English', 'ENGLISH'), ('French', 'FRENCH'), ('None', 'NONE')], default='English', max_length=8),
        ),
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ReadBookApp.models.getFileName),
        ),
    ]