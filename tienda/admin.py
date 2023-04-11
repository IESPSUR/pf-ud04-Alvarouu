from django.contrib import admin
from .models import Producto, Marca, Compra

# Register your models here.

admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Marca)
