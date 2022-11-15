from django.forms import forms
from tienda.models import Producto

class ProductosForms(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'