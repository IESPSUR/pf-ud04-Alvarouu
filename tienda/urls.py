from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/listado/', views.confirmaCompra, name='listado'),
    path('tienda/creaProducto', views.creaProducto, name='Aniadir'),
    path('tienda/CRUD', views.crud, name='CRUD'),
    path('tienda/borrado/<int:pk>', views.delete, name='borrarProducto'),
    path('tienda/editar/<int:pk>', views.edit, name='editar'),
    path('tienda/listado/confirmaCompra/<int:pk>', views.confirmaCompra, name='confirmaCompra'),
    path('tienda/informes', views.informes, name='informes'),
    path('tienda/informes/comprasUsuario', views.comprasUsuario, name='comprasUsuario'),
    path('tienda/checkout/<int:pk>', views.checkout, name='checkout'),
    path('tienda/informes/marca', views.productoMarca, name='marca'),
    path('tienda/informes/top10', views.productos10, name='top10'),
    path('tienda/informes/clientes', views.clientes, name='clientes'),
]
