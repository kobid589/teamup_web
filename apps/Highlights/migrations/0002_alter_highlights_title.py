# Generated by Django 4.0.4 on 2023-02-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Highlights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlights',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Highlights:'),
        ),
    ]
