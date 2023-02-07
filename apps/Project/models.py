from django.db import models
from uuid import uuid4
import os


def path_and_rename(instance, filename):
        upload_to = 'media/Project_Images'
        ext = filename.split('.')[-1]
        # get pic_name
        if instance.pk:
            filename = 'project_pic_{}_{}_.{}'.format(instance.pk, instance.first_name, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)


class Project(models.Model):
    description = models.CharField(verbose_name="Description", max_length=500)
    project_images = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    project_url = models.CharField(verbose_name="Project Url: ", max_length=500)

