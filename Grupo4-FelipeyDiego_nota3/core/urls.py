from django.urls import URLPattern, path
from .views import form_del_producto, form_producto, index, form_del_producto,form_mod_producto, signin, carrito, contactanos, crud, despacho, detalleproducto, perfil, signinadmin, signup, sobrenosotros

urlpatterns = [

    path ('', index, name="index"),
    path('form-producto.html', form_producto, name="form_producto"),
    path('form-del-producto.html', form_del_producto, name="form_del_producto"),
    path('form_mod_producto.html', form_mod_producto, name="form_mod_producto"),
    path ('index.html', index, name="index"),
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