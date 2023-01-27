import os
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.Address.models import Address


def path_and_rename(instance, filename):
    upload_to = 'organization/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}_{}_.{}'.format(instance.pk, instance.first_name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Organization(models.Model):
    name = models.CharField(verbose_name=_('Organization Name'), max_length=255, blank=False, null=False)
    logo = models.ImageField(verbose_name=_('Organization Logo'), upload_to=path_and_rename, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
