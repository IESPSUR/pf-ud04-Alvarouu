from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/listado/', views.muestraProducto, name='listado'),
    path('tienda/creaProducto', views.creaProducto, name='creaProducto')
]
