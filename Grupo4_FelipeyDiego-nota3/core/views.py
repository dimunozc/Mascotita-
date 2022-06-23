
from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm

# Create your views here.
def index(request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'core/index.html', datos) 

def form_producto(request):
    datos = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid:
            form.save()
            datos['mensaje'] = 'Producto agregado!.'

    return render(request, 'core/form_producto.html', datos) 

def form_del_producto(request, id):
    producto = Producto.objects.get(ProductoId = id)
    producto.delete()

    return redirect(to='index')

def form_mod_producto(request, id):
    producto = Producto.objects.get(ProductoId = id)

    datos = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid:
            form.save()
            datos['mensaje'] = 'Producto modificado!.',
    
    return render(request, 'Petshop/form_producto.html', datos) 

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
