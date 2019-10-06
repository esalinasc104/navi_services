from django.contrib import admin

from .models import Zones, CommentsZone, GeoRef


# Register your models here.
@admin.register(Zones)
class ZonesAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentsZone)
class CommentsZoneAdmin(admin.ModelAdmin):
    pass


@admin.register(GeoRef)
class GeoRefAdmin(admin.ModelAdmin):
    pass
