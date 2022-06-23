from django.db import models

# Create your models here.
class Persona(models.Model):
    PersonaId = models.IntegerField(primary_key=True, verbose_name='PersonaId')
    Rut = models.CharField(max_length=10, verbose_name='Rut')
    Nombre = models.CharField(max_length=20, verbose_name='Nombre')
    Paterno = models.CharField(max_length=20, verbose_name='Paterno')
    Materno = models.CharField(max_length=20, verbose_name='Materno')

    def __str__(self) -> str:
        return self.Nombre + ' ' + self.Paterno + ' ' + self.Materno


class Producto(models.Model):
    ProductoId = models.IntegerField(primary_key=True, verbose_name='ProductoId')
    Descripcion = models.CharField(max_length=30, verbose_name='Descripcion')
    Valor = models.IntegerField(verbose_name='Valor')
    Stock = models.IntegerField(verbose_name='Stock')

    def __str__(self) -> str:
        return self.Descripcion

class Carrito(models.Model):
    CarritoId = models.IntegerField(primary_key=True, verbose_name='ProductoId')
    Total = models.IntegerField(verbose_name='Total')
    PersonaId = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Total

class DetalleCarrito(models.Model):
    DetalleCarritoId = models.IntegerField(primary_key=True, verbose_name='DetalleCarritoId')
    ProductoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(verbose_name='Cantidad')

    def __str__(self) -> str:
        return self.Cantidad

