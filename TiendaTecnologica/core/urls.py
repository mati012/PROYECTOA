from django.urls import path
from .views import home, Producto, carrito, hardware
from django.http import HttpResponse 
 
urlpatterns = [
    path('', home, name="home"),
   
    path('Producto/<action>/<id>', Producto, name="producto"),
    path('carrito', carrito, name="carrito"),
    path( 'hardware', hardware, name="hardware"),
   
]
