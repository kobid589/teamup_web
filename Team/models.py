import os
from uuid import uuid4

from django.db import models

def team_path(instance, filename):
    upload_to = '/media'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'team_photo{}_{}_.{}'.format(instance.pk, instance.first_name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=255)

    description= models.CharField(max_length=255 , null=True, blank=True)
    logo= models.ImageField(upload_to=team_path, null=True, blank=True)


