from django import forms
from django.contrib.auth.models import User

from .models import Producto, Compra, Marca


class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'modelo', 'unidades', 'precio', 'detalles', 'marca']


class FiltroForm(forms.ModelForm):
    nombre = forms.CharField(required=False)

    class Meta:
        model = Producto
        fields = ['nombre']


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['unidades']


class CheckoutForm(forms.ModelForm):
    unidades = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Compra
        fields = ['unidades']


class UsuarioForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)


class MarcaForm(forms.Form):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), required=False)

