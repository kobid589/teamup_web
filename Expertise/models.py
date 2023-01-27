from django.db import models

# Create your models here.
class ExpertiseField(models.Model):

    Field_of_Expertise = models.CharField(max_length=10)
    Experience_Years = models.CharField(max_length=10)
