# Generated by Django 4.2.5 on 2023-09-19 15:38

import ReadBookApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReadBookApp', '0013_alter_genre_image_addcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ReadBookApp.models.getFileName),
        ),
    ]
