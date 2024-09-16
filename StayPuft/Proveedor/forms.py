#  el forms es para que me acepte los coampos que tengo en todos los modelos foem.html-->sean mas simples
from django import forms
from .models import Proveedor
class ProveedorForm(forms.ModelForm):
    class Meta:
        model= Proveedor
        fields='__all__'