import os
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


def path_and_rename(instance, filename):
    upload_to = 'media/org_images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'org_image_{}_{}_.{}'.format(instance.pk, instance.first_name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Organization(models.Model):
    name = models.CharField(verbose_name=_('Organization Name'), max_length=255, blank=False, null=False)
    logo = models.ImageField(verbose_name=_('Organization Logo'), upload_to=path_and_rename, null=True, blank=True)
    description = models.CharField(verbose_name=_('Organization Description'), max_length=255, blank=True, null=True)
    established_date = models.DateField(verbose_name="Established On:", blank=True, null=True)
