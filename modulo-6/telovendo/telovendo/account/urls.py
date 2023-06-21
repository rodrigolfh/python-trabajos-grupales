from django.urls import path
from . import views # para que más abajo se pueda usar views.index
urlpatterns = [
    path("", views.index, name = "index"),
    path("pg2", views.pg2, name = "pg2"),
    path("inscripcion", views.crear_proveedor, name = "inscripcion"),
    path("login", views.login_view, name="login"),
    path("bienvenida", views.bienvenida_view, name="bienvenida"),
    path('forms', views.forms, name='forms'), 
    path("logout", views.logout_view, name="logout"),
    path('registro_cliente', views.cliente_form_view, name='registro_cliente'), 
    #path("usuarios", views.usuarios, name = "usuarios")
    # "" es lo que sigue de la url principal, en este caso es solo /, 
    # el segundo parámetro es lo que se debe renderizar al ingresar allí.
    #el tercer parámetro es para poder referenciar desde otras partes de la app.
]