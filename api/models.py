# Create your models here.
from django import forms
from djongo import models


class CoordinateZone(models.Model):
    longitude = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True


class GeoRef(models.Model):
    code = models.CharField(max_length=8, editable=False, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "geo_ref"
        verbose_name = "Referencia Geografica"
        verbose_name_plural = "Referencias Geograficas"


class Zones(models.Model):
    zones_state_choices = [
        ("1", "ACTIVO"),
        ("0", "INACTIVO"),
        ("2", "NO DISPONIBLE")
    ]
    zone_type = [
        ("1", "COLONIA"),
        ("2", "BARRIO"),
        ("3", "PASAJE"),
        ("4", "CANTON"),
        ("5", "CASERI0"),
    ]
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    location = models.ForeignKey(GeoRef, to_field="code", null=True, on_delete=models.CASCADE)
    state = models.CharField(max_length=2, choices=zones_state_choices, default="2")
    geo_type = models.CharField(max_length=2, choices=zone_type, default="1")
    coordinates = models.ArrayModelField(model_container=CoordinateZone, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "zones"
        verbose_name = "Zona"
        ordering = ["name"]


class DangerRangeZone(models.Model):
    danger_range = [
        (1, "Nivel 1 - Todo para ir bien"),
        (2, "Nivel 2 - Conduzcase con cuidado"),
        (3, "Nivel 3 - Mantengase alerta"),
        (4, "Nivel 4 - Si puede evite la zona"),
        (5, "Nivel 5 - No ingrese a la zona"),
    ]

    _id = models.ObjectIdField()
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE, verbose_name="Elige la zona")

    code_danger = models.IntegerField(default=1, verbose_name='Nivel', choices=danger_range)

    is_presencia_de_delincuentes = models.BooleanField(verbose_name="Existe presencia de delincuentes en la zona")
    is_ingresar_a_la_zona_controlado = models.BooleanField(
        verbose_name="Ingresar a la zona es controlado por pandillas")
    is_existe_renta_por_entrar_habitar = models.BooleanField(
        verbose_name="Existe algun tipo de renta para entrar o habitar a la zona")
    is_drogas = models.BooleanField(verbose_name="Se rumora de ventas de drogas en la zona")
    hora_minima = models.TimeField(verbose_name="Desde")
    hora_maxima = models.TimeField(verbose_name="Hasta")

    asesinatos = models.BooleanField()
    robo_asaltos = models.BooleanField()
    agresion_acoso = models.BooleanField()
    robo_autos = models.BooleanField()
    acoso_sexual = models.BooleanField()
    vandalismo = models.BooleanField()

    added = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "zones_danger_rates"
        verbose_name = "Indice de peligro"
        verbose_name_plural = "Indices de peligro"

    def __str__(self):
        return self.zone.name

    @property
    def location(self):
        return '' + self.zone.location.name + "\n si cambias la zona, guarda nuevamente para actualizar este valor automaticamente"


class DangerRangeZoneForm(forms.ModelForm):
    class Meta:
        model = DangerRangeZone
        fields = "__all__"

    def filter_zones(self):
        return Zones.objects.filter(location__code__startswith="10")

    def __init__(self, *args, **kwargs):
        super(DangerRangeZoneForm, self).__init__(*args, **kwargs)
        self.fields['zone'].queryset = self.filter_zones()


class CommentsZone(models.Model):
    _id = models.ObjectIdField()
    date = models.DateTimeField(auto_created=True)
    txt = models.TextField()
    user = models.CharField(max_length=100)
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)

    class Meta:
        db_table = "zones_comments"
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.txt
