from django.urls import path
from . import views # para que más abajo se pueda usar views.index
urlpatterns = [
    path("", views.index, name = "index"),
    path("pg2", views.pg2, name = "pg2"),
    path("inscripcion", views.crear_proveedor, name = "inscripcion")
    #path("usuarios", views.usuarios, name = "usuarios")
    # "" es lo que sigue de la url principal, en este caso es solo /, 
    # el segundo parámetro es lo que se debe renderizar al ingresar allí.
    #el tercer parámetro es para poder referenciar desde otras partes de la app.
]