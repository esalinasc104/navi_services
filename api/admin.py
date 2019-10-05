from django.contrib import admin
from .models import Zones


# Register your models here.
@admin.register(Zones)
class ZonesAdmin(admin.ModelAdmin):
    pass