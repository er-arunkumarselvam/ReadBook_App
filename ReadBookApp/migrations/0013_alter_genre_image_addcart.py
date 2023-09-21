# Generated by Django 4.2.5 on 2023-09-19 11:37

import ReadBookApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReadBookApp', '0012_remove_bookproduct_translatorname_alter_genre_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ReadBookApp.models.getFileName),
        ),
        migrations.CreateModel(
            name='AddCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReadBookApp.bookproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]