from django.urls import URLPattern, path
from .views import index ,signin, carrito, contactanos, crud, despacho, detalleproducto, perfil, signinadmin, signup, sobrenosotros

urlpatterns = [
    path ('', index, name="inicio"),
    path ('index.html', index, name="inicio"),
    path('signin.html', signin, name="login"),
    path('carrito.html', carrito, name="carrito"),
    path('contactanos.html', contactanos, name="contactanos"),
    path('crud.html', crud, name="crud"),
    path('despacho.html', despacho, name="despacho"),
    path('detalleproducto.html', detalleproducto, name="detalleproducto"),
    path('perfil.html', perfil, name="perfil"),
    path('signinadmin.html', signinadmin, name="signinadmin"),
    path('signup.html', signup, name="signup"),
    path('sobrenosotros.html', sobrenosotros, name="sobrenosotros"),
]