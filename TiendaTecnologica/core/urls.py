from django.urls import path
from .views import home, Producto, carrito, hardware,acercade,contacto,iniciosesion,notebooks,politicaprivacidad,registro,terminocondiciones 
from django.http import HttpResponse 
 
urlpatterns = [
    path('', home, name="home"),
   
    path('Producto/<action>/<id>', Producto, name="producto"),
    path('carrito', carrito, name="carrito"),
    path( 'hardware', hardware, name="hardware"),
    path( 'acercade', acercade, name="acercade"),
    path( 'contacto', contacto, name="contacto"),
    path( 'iniciosesion', iniciosesion, name="iniciosesion"),
    path( 'notebooks', notebooks, name="notebooks"),
    path( 'politicaprivacidad', politicaprivacidad, name="politicaprivacidad"),
    path( 'registro', registro, name="registro"),
    path( 'terminnocondiciones', terminocondiciones, name="terminocondiciones"),
    
   
]
