from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from apps.NepalAdministrativeDivision.models import ProvincesDetail, DistrictDetail, MunicipalityDetail, WardDetail


class Address(models.Model):
    province = models.ForeignKey(ProvincesDetail, blank=True, null=True,
                                 on_delete=models.SET_NULL, related_name='addresses')
    district = models.ForeignKey(DistrictDetail, blank=True, null=True,
                                 on_delete=models.SET_NULL, related_name='addresses'
                                 )
    municipality = models.ForeignKey(MunicipalityDetail, blank=True, null=True,
                                     on_delete=models.SET_NULL, related_name='addresses'
                                     )
    ward = models.ForeignKey(WardDetail, blank=True, null=True,
                             on_delete=models.SET_NULL, related_name='addresses'
                             )
    street = models.CharField(verbose_name=_('Street'), max_length=255, blank=True, null=True),
    tole = models.CharField(verbose_name=_('Tole'), max_length=255, blank=True, null=True),

    is_current_address = models.BooleanField(verbose_name=_('Is Current Address'), default=True)
