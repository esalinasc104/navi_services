# Create your models here.
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
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    location = models.ForeignKey(GeoRef, to_field="code", null=True, on_delete=models.CASCADE)
    state = models.IntegerField()
    geo_type = models.CharField(max_length=5)
    coordinates = models.ArrayModelField(model_container=CoordinateZone)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "zones"
        verbose_name = "Zona"


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
