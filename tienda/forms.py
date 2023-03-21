from django import forms
from .models import Producto


class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"