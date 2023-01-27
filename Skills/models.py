from django.db import models

# Create your models here.
class InputSkill(models.Model):
    skill_name = models.CharField(max_length=10)
    skill_level= models.CharField(max_length=10)