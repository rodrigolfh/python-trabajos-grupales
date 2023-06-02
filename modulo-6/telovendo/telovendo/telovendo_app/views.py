from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

#def index(request): #paso 2. request representa el request que hace el usuario al servidor. se debe importar httpresponse.
    
#    return HttpResponse("Bievenidos a Telovendo")

def index(request):
    return(render(request, "telovendo_app/index.html")) #se agrega render para indicar que debe renderizar el template indicado

