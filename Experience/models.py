from django.db import models
from apps.Organization.models import Organization
from apps.Highlights.models import Highlights
# Create your models here.
class Experience(models.Model):
    From= models.DateField( null=True , blank=True)
    To= models.DateField(null= True , blank= True)
    description= models.CharField(max_length=255, null=True, blank=True)

    organization=models.ForeignKey(Organization, null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='organization')

    highlights= models.ForeignKey(Highlights,null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='highlights')