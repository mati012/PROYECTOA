from django.urls import path
from .views import home, Producto, carrito 
 
urlpatterns = [
    path('', home, name="home"),
   
    path('Producto/<action>/<id>', Producto, name="producto"),
    path('carrito', carrito, name="carrito"),
   
]
