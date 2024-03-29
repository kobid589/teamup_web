# Generated by Django 4.0.4 on 2023-03-16 07:05

import apps.Skill.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Skill', '0003_rename_inputskill_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill_level',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill_name',
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.Skill.models.skill_path),
        ),
        migrations.AddField(
            model_name='skill',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_skill', to=settings.AUTH_USER_MODEL),
        ),
    ]
