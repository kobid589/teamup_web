# Generated by Django 4.0.4 on 2023-02-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputskill',
            name='skill_level',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='inputskill',
            name='skill_name',
            field=models.CharField(max_length=255),
        ),
    ]