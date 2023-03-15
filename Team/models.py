import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

from apps.Individual.models import Individual


def team_path(instance, filename):
    upload_to = '/media'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'team_photo_{}_.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to=team_path, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    members = models.ManyToManyField(Individual, related_name='team_members', null=True, blank=True)

    def __str__(self):
        return '%s' % self.name
