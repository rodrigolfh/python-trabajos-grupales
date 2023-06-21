from django import forms
from .models import Proveedor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
"""
    razon_social = models.CharField(max_length=50)
    rut_empresa = models.CharField(max_length=13)
    contacto = models.CharField(max_length=50)
    email_contacto = models.EmailField(verbose_name="Mail de contacto", unique=True)
    telefono_contacto = models.CharField(max_length=15, default="")
    fecha_inscripcion = models.DateField(datetime.date.today())
"""

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__' 


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput)
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}