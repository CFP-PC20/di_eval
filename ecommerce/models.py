from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class Articulo(models.Model):
    nombre = models.CharField(max_length=80)
    precio = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    descripcion = models.TextField()
    imagen = models.FilePathField(path="/img")

    def __str__(self):
        return self.nombre
