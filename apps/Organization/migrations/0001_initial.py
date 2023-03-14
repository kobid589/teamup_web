# Generated by Django 4.0.4 on 2023-01-23 06:22

import apps.Organization.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Organization Name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=apps.Organization.models.path_and_rename, verbose_name='Organization Logo')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Address.address')),
            ],
        ),
    ]
