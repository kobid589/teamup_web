import os
from uuid import uuid4

import nepali_datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.Address.models import Address
from core.model_constants import GENDER, RELIGIONS, ETHNICITY


def path_and_rename(instance, filename):
    upload_to = 'individual/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}_{}_.{}'.format(instance.pk, instance.first_name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Individual(models.Model):
    # General information
    first_name = models.CharField(verbose_name=_('First  Name'), max_length=100)
    middle_name = models.CharField(verbose_name=_('Middle  Name'), max_length=100, blank=True)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=100)

    gender = models.CharField(max_length=1, choices=GENDER)
    photo = models.ImageField(upload_to=path_and_rename, null=True, blank=True)

    # Contact
    email = models.EmailField(verbose_name=_('Email'), max_length=255, blank=True, null=True)
    contact = models.TextField(verbose_name=_('Contact'), max_length=255, blank=True, null=True)

    # Other information
    # organization = models.ForeignKey()
    remarks = models.TextField(verbose_name=_('Remarks'), max_length=255, blank=True, null=True)
    religions = models.CharField(verbose_name=_('Religions'), max_length=255, choices=RELIGIONS)
    ethnicity = models.CharField(verbose_name=_('Ethnicity'), max_length=255, choices=ETHNICITY)
    # date_of_birth = models.DateField(verbose_name=_('Date of Birth'), blank=True, null=True)
    created_date = models.DateField(verbose_name=_('Time of Death'), auto_now=True)

    #
    address = models.ForeignKey(Address, blank=True, null=True,
                                on_delete=models.SET_NULL, related_name='addresses')
    # def __str__(self):
    #     return '%s' % (
    #             self.first_name + ' - (ID : ' + self.id.__str__() + ', Generation : ' + self.get_level().__str__() + ')')

    class MPTTMeta:
        order_insertion_by = ['level']

    @staticmethod
    def get_maximum_height():
        max_level = 0
        if Individual.objects.count() > 0:
            max_level = max(Individual.objects.all(), key=lambda x: x.level).level + 1
        return max_level

    # @property
    # def date_of_birth_in_bs(self):
    #     """converts bs to ad"""
    #     dob = ''
    #     try:
    #         if self.date_of_birth:
    #             dob = nepali_datetime.datetime.from_datetime_date(self.date_of_birth)
    #     except Exception as e:
    #         print('Exception raised::', e)
    #     return dob
