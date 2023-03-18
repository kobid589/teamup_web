from apps.NepalAdministrativeDivision.imports import *
from django.utils.translation import gettext_lazy as _

from django.utils.translation import get_language as LANGUAGE_CODE


class ProvincesDetail(models.Model):
    """ province """

    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')

    name = models.CharField(_('name'), max_length=200, default="")
    name_eng = models.CharField(_('name_eng'), max_length=200, default="")
    state_number = models.CharField(_('state_number'), max_length=20, default="")

    def __str__(self):
        if LANGUAGE_CODE() == 'ne':
            return self.name
        else:
            return self.name_eng


class DistrictDetail(models.Model):
    """districts"""

    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('Districts')

    id = models.IntegerField(_('id'), primary_key=True)
    name = models.CharField(_('name'), max_length=200, default="")
    name_eng = models.CharField(_('name_eng'), max_length=200, default="")
    state_id = models.ForeignKey(ProvincesDetail, related_name='related_districts', on_delete=models.CASCADE)

    def __str__(self):
        if LANGUAGE_CODE() == 'ne':
            return self.name
        else:
            return self.name_eng


class MunicipalityDetail(models.Model):
    """municipalities"""

    class Meta:
        verbose_name = _('Municipality')
        verbose_name_plural = _('Municipalities')

    id = models.IntegerField(_('id'), primary_key=True)
    district_id = models.ForeignKey(DistrictDetail, related_name='related_municipalities', on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=200, default="")
    name_eng = models.CharField(_('name_eng'), max_length=200, default="")
    locallevel_type = models.CharField(_('locallevel_type'), max_length=200, default="")
    wards = models.IntegerField(_('wards'), blank=True, null=True)
    locallevel_code = models.IntegerField(_('locallevel_code'))

    def __str__(self):
        if LANGUAGE_CODE() == 'ne':
            return self.name
        else:
            return self.name_eng


class WardDetail(models.Model):
    """
            Stores information about ward within a municipality
    """
    municipality = models.ForeignKey(MunicipalityDetail, related_name="related_wards", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        if LANGUAGE_CODE() == 'ne':
            return self.name
        else:
            return self.name_eng
