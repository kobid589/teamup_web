# Generated by Django 4.0.4 on 2023-03-14 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Experience', '0003_experience_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='person',
        ),
    ]
