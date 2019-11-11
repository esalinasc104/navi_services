# Create your models here.
from django import forms
from djongo import models


class CoordinateZone(models.Model):
    longitude = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True

    def as_json(self):
        return dict(
            lng=self.longitude,
            lat=self.latitude
        )


class GeoRef(models.Model):
    code = models.CharField(max_length=8, editable=False, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def as_json(self):
        return dict(
            code=self.code,
            name=self.name
        )

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

    def as_json(self, get_coordinates=True):
        list_coordinates = []
        if get_coordinates:
            list_coordinates = [ob.as_json() for ob in self.coordinates]
        return dict(
            _id=str(self._id),
            name=self.name,
            location=self.location.as_json(),
            state=self.state,
            geo_type=self.geo_type,
            coordinates=list_coordinates
        )

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

    added = models.DateTimeField(auto_now_add=True)
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

    def as_json(self):
        crimes = {
            "asesinatos": self.asesinatos,
            "robo_asaltos": self.robo_asaltos,
            "agresion_acoso": self.agresion_acoso,
            "robo_autos": self.robo_autos,
            "acoso_sexual": self.acoso_sexual,
            "vandalismo": self.vandalismo
        }
        return dict(
            id=str(self._id),
            zone=self.zone.as_json(get_coordinates=False),
            level_danger=self.code_danger,
            is_presencia_de_delincuentes=self.is_presencia_de_delincuentes,
            is_ingresar_a_la_zona_controlado=self.is_ingresar_a_la_zona_controlado,
            is_existe_renta_por_entrar_habitar=self.is_existe_renta_por_entrar_habitar,
            is_drogas=self.is_drogas,
            hora_minima=self.hora_minima,
            hora_maxima=self.hora_maxima,
            crimenes=crimes
        )

    def parser_to_obj(self, form):
        self.zone = Zones.objects.get(_id=form.get('zone'))
        self.code_danger = form.get("level_danger")
        self.is_presencia_de_delincuentes = form.get("is_presencia_de_delincuentes")
        self.is_ingresar_a_la_zona_controlado = form.get("is_ingresar_a_la_zona_controlado")
        self.is_existe_renta_por_entrar_habitar = form.get("is_existe_renta_por_entrar_habitar")
        self.is_drogas = form.get("is_drogas")
        self.hora_minima = form.get("hora_minima")
        self.hora_maxima = form.get("hora_maxima")
        self.asesinatos = form.get("asesinatos")
        self.robo_asaltos = form.get("robo_asaltos")
        self.agresion_acoso = form.get("agresion_acoso")
        self.robo_autos = form.get("robo_autos")
        self.acoso_sexual = form.get("acoso_sexual")
        self.vandalismo = form.get("vandalismo")


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
