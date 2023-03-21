
from django.db import models


# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    unidades = models.IntegerField('Unidades')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.CharField(max_length=500)
    marca = models.ForeignKey(Marca, models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.marca)


class Compra(models.Model):

    producto = models.ForeignKey(Producto, models.PROTECT)
    user = models.CharField(max_length=30)
    fecha = models.DateField('Fecha')
    unidades = models.IntegerField('Unidades')
    importe = models.DecimalField(max_digits=10, decimal_places=2)
