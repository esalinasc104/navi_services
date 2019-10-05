

# Create your models here.
from djongo import models


class Zones(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    geo_ref = models.CharField(max_length=8)
    state = models.IntegerField()
    geo_type = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "zones"
        verbose_name = "Zona"
