from django.db import models


# Create your models here.


class Individual(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.first_name
