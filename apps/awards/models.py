from django.db import models
from uuid import uuid4
import os


def path_and_rename(instance, filename):
    upload_to = 'media/award_images'
    ext = filename.split('.')[-1]
    # get pic_name
    if instance.pk:
        filename = 'award_pic_{}_{}_.{}'.format(instance.pk, instance.first_name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Awards(models.Model):
    title = models.CharField(verbose_name="Award Title", max_length=255)
    description = models.CharField(verbose_name="Description", max_length=500,)
    awarded_on = models.DateField(verbose_name="Awarded On:")
    award_logo = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    award_images = models.ImageField(upload_to=path_and_rename, null=True, blank=True)


