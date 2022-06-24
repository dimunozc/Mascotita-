
from ast import If
from django.shortcuts import render, redirect
from matplotlib.pyplot import table
from requests import post
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    Producto= Producto.object.all()

    datos = {
        'productos': Producto
    }
    return render(request, 'core/table.html', datos)

def form_producto(request):
    datos = {
        'form': ProductoForm()

    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos ['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_producto.html', datos)


def form_mod_producto(request, id):
    Producto = Producto.object.get(ProductoId=id)
    datos = {
        'form': ProductoForm(instance=Producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=Producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'core/form_mod_producto', datos)

def for_del_vehiculo(request, id):
    Producto = Producto.object.get(ProductoId=id)
    Producto.delete()
    return redirect(to=table)

def signin(request):
    return render(request, 'core/signin.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def contactanos(request):
    return render(request, 'core/contactanos.html')
    
def crud(request):
    return render(request, 'core/crud.html')

def despacho(request):
    return render(request, 'core/despacho.html')

def detalleproducto(request):
    return render(request, 'core/detalleproducto.html')

def perfil(request):
    return render(request, 'core/perfil.html')

def signinadmin(request):
    return render(request, 'core/signinadmin.html')

def signup(request):
    return render(request, 'core/signup.html')

def sobrenosotros(request):
    return render(request, 'core/sobrenosotros.html')
