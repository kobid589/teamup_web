import os
from uuid import uuid4

from django.db import models

def language_path(instance, filename):
    upload_to = '/media'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'language_photo{}_{}_.{}'.format(instance.pk, instance.first_name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
# Create your models here.
class ProgrammingLanguage(models.Model):
    title= models.CharField(max_length=255 , null=True , blank= True)
    description= models.CharField(max_length=255, null=True, blank=True)
    image= models.ImageField(upload_to=language_path ,  null=True, blank=True)