from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

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
