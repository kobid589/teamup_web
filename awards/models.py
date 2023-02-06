from django.db import models


class Awards(models.Model):
    title = models.CharField(verbose_name="Award Title", max_length=255)
    description = models.CharField(verbose_name="Description", max_length=500)
    awarded_on = models.DateField(verbose_name="Awarded On:")


