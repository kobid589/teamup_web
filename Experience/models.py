from django.db import models

# Create your models here.
class Experience(models.Model):
    From= models.DateField( null=True , blank=True)
    To= models.DateField(null= True , blank= True)
    description= models.CharField(max_length=255, null=True, blank=True)

