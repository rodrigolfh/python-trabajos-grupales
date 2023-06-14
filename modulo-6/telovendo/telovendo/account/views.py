from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib import messages
# Create your views here.
def index(request):
    
    users = User.objects.all()
    return render(request, 'account/index.html')

def pg2(request):
    users = User.objects.all()
    return render(request, 'account/pg2.html', { 'users':users})

#-------------------------------------------------------------------
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

