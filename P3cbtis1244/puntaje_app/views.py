from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,"index.html")

def contactos(request):
    return render(request,"contactos.html")

def empleados(request):
    return render(request,"empleados.html")

def sucursal(request):
    return render(request,"sucursal.html")

def ventas(request):
    return render(request,"ventas.html")

def productos(request):
    return render(request,"productos.html")

def encargado(request):
    return render(request,"encargado.html")