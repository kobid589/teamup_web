from django.db import models

# Create your models here.
class Skills(models.Model):
    skill_name = models.CharField(max_length=255)
    skill_level= models.CharField(max_length=255)