# Generated by Django 4.0.4 on 2023-02-07 09:08

import apps.awards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Award Title')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('awarded_on', models.DateField(verbose_name='Awarded On:')),
                ('award_logo', models.ImageField(blank=True, null=True, upload_to=apps.awards.models.path_and_rename)),
                ('award_images', models.ImageField(blank=True, null=True, upload_to=apps.awards.models.path_and_rename)),
            ],
        ),
    ]
