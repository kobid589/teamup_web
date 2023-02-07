from django.db import models

# Create your models here.
class login(models.Model):
    username_email=models.CharField(verbose_name=('Username/Email'), max_length=255)
    password = models.CharField(max_length=255)

