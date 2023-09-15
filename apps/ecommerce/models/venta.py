from django.db import models

from apps.ecommerce.models.producto import Prodcuto
from apps.default.models.base_model import BaseModel


class Venta(BaseModel):

    producto = models.ForeignKey(Prodcuto, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
