from django.db import models

from apps.default.models.base_model import BaseModel

class Prodcuto(BaseModel):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=350)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
