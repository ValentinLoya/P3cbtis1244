from django.urls import path
from . import views
urlpatterns = [
    path("" ,views.index,name="index"),
    path("contactos/" ,views.contactos,name="contactos"),
    path("empleados/" ,views.empleados,name="empleados"),
    path("sucursal/" ,views.sucursal,name="sucursal"),
    path("ventas/" ,views.ventas,name="ventas"),
    path("productos/" ,views.productos,name="productos"),
    path("encargado/" ,views.encargado,name="encargado"),
]