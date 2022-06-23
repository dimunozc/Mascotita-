from django.contrib import admin
from .models import Carrito, DetalleCarrito, Persona, Producto

# Register your models here.
admin.site.register(Persona)
admin.site.register(Carrito)
admin.site.register(DetalleCarrito)
admin.site.register(Producto)
