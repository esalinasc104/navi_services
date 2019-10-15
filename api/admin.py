from django.contrib import admin

from api.models import Zones, CommentsZone, GeoRef, DangerRangeZone, DangerRangeZoneForm


# Register your models here.
@admin.register(Zones)
class ZonesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'state', 'geo_type')
    search_fields = ['name', 'location__name']
    list_filter = ('state', 'geo_type')

    def get_queryset(self, request):
        return Zones.objects.filter(location__code__startswith="10")


@admin.register(CommentsZone)
class CommentsZoneAdmin(admin.ModelAdmin):
    pass


@admin.register(GeoRef)
class GeoRefAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')


@admin.register(DangerRangeZone)
class DangerRangeZoneAdmin(admin.ModelAdmin):
    add_form_template = "admin/danger_range_add_template.html"
    view_on_site = False
    form = DangerRangeZoneForm
    autocomplete_fields = ['zone']
    readonly_fields = ['location']
    fieldsets = (
        ('Zona a reportar', {
            'fields': ['zone', 'location']
        }),
        ('Nivel de inseguridad', {
            'fields': ['code_danger']
        }),
        ('Riesgos', {
            'fields': ['is_presencia_de_delincuentes',
                       'is_ingresar_a_la_zona_controlado',
                       'is_existe_renta_por_entrar_habitar',
                       'is_drogas']
        }
         ),
        ('Rango de horario para movilizarse en la zona', {
            'fields': ['hora_minima', 'hora_maxima']
        }),
        ('Delitos comunes en la zona', {
            'fields': ['asesinatos', 'robo_asaltos',
                       'agresion_acoso', 'robo_autos', 'acoso_sexual', 'vandalismo']
        })
    )

    def add_view(self, request, form_url='', extra_context=None):
        return super(DangerRangeZoneAdmin, self).add_view(request, form_url, extra_context)
