# Generated by Django 4.2.5 on 2023-09-16 10:25

import ReadBookApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReadBookApp', '0004_alter_bookproduct_bookdecription_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='decription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ReadBookApp.models.getFileName),
        ),
    ]
