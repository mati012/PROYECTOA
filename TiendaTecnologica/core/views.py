
from django.shortcuts import redirect, render
from .models import Producto, Categoria
from .forms import ProductoForm
from django.http import HttpRequest
 
# Create your views here.
 
def home(request):
    return render(request, "core/home.html")
 
def carrito(request):
    data = {"list": carrito.objects.all().order_by('nombre')}
    return render(request, "core/carrito.html", data)
 

 
def Producto(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "idProducto": id}
 
    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                
                    form.save()
                    data["mesg"] = "Producto guardado"
                
 
    elif action == 'upd':
        objeto = Producto.objects.get(idproducto=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
         
        data["form"] = ProductoForm(instance=objeto)
 
    elif action == 'del':
    
            Producto.objects.get(patente=id).delete()
            data["mesg"] = "Producto eliminado"
            return redirect(Producto, action='ins', id = '-1')
        
 
    data["list"] = Producto.objects.all().order_by('nombre')
    return render(request, "core/Producto.html", data)
def hardware(request):
    return render(request, "core/hardware.html") 
def acercade(request):
    return render(request, "core/AcercaDe.html")  
def contacto(request):
    return render(request, "core/contacto.html")  
def iniciosesion(request):
    return render(request, "core/InicioSesion.html")
def notebooks(request):
    return render(request, "core/Notebooks.html")
def politicaprivacidad(request):
    return render(request, "core/PoliticaPrivacidad.html")
def registro(request):
    return render(request, "core/Registro.html")
def terminocondiciones(request):
    return render(request, "core/TerminoCondiciones.html")


def poblar_bd(request):
    Producto.objects.all().delete()
    Producto.objects.create(IdProducto="AAA", Nombre='HP Omen 15-EN0002LA', Precio="1249990", imagen="images/Asus-TUF NOTEBOOK 3.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(IdProducto="BBB", Nombre='ASUS Chromebook C423NA-WB04', Precio="209900", imagen="images/Noteebook 1.jpg", categoria=Categoria.objects.get(idCategoria=1))



    return redirect(Producto, action='ins', id = '-1')

