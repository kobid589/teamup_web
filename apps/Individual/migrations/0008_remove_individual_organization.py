# Generated by Django 4.0.4 on 2023-02-07 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Individual', '0007_merge_20230207_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='organization',
        ),
    ]