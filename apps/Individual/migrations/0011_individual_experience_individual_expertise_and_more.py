# Generated by Django 4.0.4 on 2023-03-14 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Experience', '0004_remove_experience_person'),
        ('Expertise', '0003_remove_expertise_experience_years_and_more'),
        ('ProgrammingLanguage', '0001_initial'),
        ('Team', '0001_initial'),
        ('Individual', '0010_remove_individual_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experience', to='Experience.experience'),
        ),
        migrations.AddField(
            model_name='individual',
            name='expertise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expertise', to='Expertise.expertise'),
        ),
        migrations.AddField(
            model_name='individual',
            name='programming_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='langaugeinfo', to='ProgrammingLanguage.programminglanguage'),
        ),
        migrations.AddField(
            model_name='individual',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team', to='Team.team'),
        ),
    ]