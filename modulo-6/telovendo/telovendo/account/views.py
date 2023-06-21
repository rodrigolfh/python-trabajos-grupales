from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Proveedor
from .forms import ProveedorForm, UserRegistrationForm, ClientRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    
    users = User.objects.all()
    return render(request, 'account/index.html')

@login_required(login_url="/account/login")
def pg2(request):
    users = User.objects.all()
    return render(request, 'account/pg2.html', { 'users':users})

#-------------------------------------------------------------------

@login_required(login_url="/account/login")
def crear_proveedor(request):
    form = ProveedorForm()

    if request.method == "POST":
        print(request)
        form = ProveedorForm(request.POST)

        if form.is_valid():
            print(form)
            proveedor = Proveedor()
            proveedor.razon_social = form.cleaned_data['razon_social']
            proveedor.rut_empresa = form.cleaned_data['rut_empresa']
            proveedor.contacto = form.cleaned_data['contacto']
            proveedor.email_contacto = form.cleaned_data['email_contacto']
            proveedor.telefono_contacto = form.cleaned_data['telefono_contacto']
            proveedor.fecha_inscripcion = form.cleaned_data['fecha_inscripcion']
            proveedor.save()
            messages.success(request, 'Usuario ingresado exitosamente')
        else:
            print("Datos invalidos")
        return redirect('account/')
    
    context = {
        'form': form
    }
    
    return render(request, 'account/inscripcion.html', context=context)

def login_view(request):
    if 'next' in request.GET:
        #si en la url está la palabra "next", generada al redirigir desde @login_required, enviar mensaje.
        messages.add_message(request, messages.INFO, 'Acceso restringido, debe autenticarse para acceder al recurso solicitado')


    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            
            login(request, user)
          
            return HttpResponseRedirect(reverse("bienvenida"))
        else:
            context= ["Credenciales Inválidas"]#si no lo hago como lista, itera por cada caracter del string.
            return render(request, "account/login.html", {"messages": context})

    return render(request, "account/login.html") #view del login

@login_required(login_url="/account/login")
def bienvenida_view(request):
    
    return render(request, 'account/bienvenida.html')

@login_required(login_url="/account/login")
def logout_view(request):
    
    logout(request)
    return render(request, "account/logout.html")


@permission_required('Administradores', login_url='index', raise_exception=True) 
def forms(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            group = form.cleaned_data['group']
            user = form.save()
            user.groups.add(group)
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('index') #requiere import de django shortcuts (redirect)
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'account/formulario.html', context=context)

def cliente_form_view(request):
    if request.method == "POST":
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            group = form.cleaned_data['group']
            user = form.save()
            user.groups.add(group)
            messages.success(request, f'Cliente {username} creado exitosamente!!')
            return redirect('index') #requiere import de django shortcuts (redirect)
    else:
        form = ClientRegistrationForm()

    context = {'form': form}
    return render(request, 'account/formulario_cliente.html', context=context)