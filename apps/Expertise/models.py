import os
from uuid import uuid4

from django.db import models


def path_and_rename(instance, filename):
    upload_to = 'media'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}_{}_.{}'.format(instance.pk, instance.first_name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.
class Expertise(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=255, default=" ")
    description = models.CharField(max_length=255, default=" ")
=======
    name = models.CharField(max_length=255 , default=' ')
    description = models.CharField(max_length=255, default=' ')
>>>>>>> ea34e78404be3ba9dd6824f127cb1a6bcc5dc16e
    photo = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
