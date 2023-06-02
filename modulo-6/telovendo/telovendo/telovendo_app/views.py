from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

def index(request): #paso 2. request representa el request que hace el usuario al servidor. se debe importar httpresponse.
    
    return HttpResponse("Bievenidos a Telovendo")

#ahora CREAR urls.py en carpeta de la app.