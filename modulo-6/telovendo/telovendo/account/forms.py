from django import forms
from .models import Proveedor
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