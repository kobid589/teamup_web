import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


def skill_path(instance, filename):
    upload_to = '/media'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'skill_photo_{}_.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to=skill_path, null=True, blank=True)
    users = models.ManyToManyField(User, related_name='user_skill', null=True, blank=True)

    def __str__(self):
        return '%s' % self.name + str(self.id)
