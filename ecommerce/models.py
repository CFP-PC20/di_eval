from django.db import models
from django.conf import settings

# Create your models here.

class Articulo(models.Model):
    nombre = models.CharField(max_length=80)
    precio = models.FloatField()
    descripcion = models.TextField()
    imagen = models.FilePathField(path="/img")

    def __str__(self):
        return self.nombre
