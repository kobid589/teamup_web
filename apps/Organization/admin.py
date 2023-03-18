from django.contrib import admin

# Register your models here.
from apps.Organization.models import Organization

admin.site.register(Organization)
