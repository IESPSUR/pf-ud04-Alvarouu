from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages
from .forms import productoForm, FiltroForm, CompraForm, UsuarioForm
from tienda.models import Producto, Marca, Compra
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def welcome(request):

    return render(request,'tienda/index.html', {})


def crud(request):
    prod = Producto.objects.all()

    return render(request, 'tienda/CRUD.html', {'prod':prod})


def creaProducto(request):

    formulario = productoForm()

    if request.method == 'POST':
        nombre = request.POST['nombre']
        modelo = request.POST['modelo']
        unidades = request.POST['unidades']
        precio = request.POST['precio']
        detalles = request.POST['detalles']
        nombre_marca = request.POST['marca']
        marca = Marca.objects.get(nombre=nombre_marca)
        obj = Producto.objects.create(nombre=nombre, modelo=modelo,
                                      unidades=unidades, precio=precio,
                                      detalles=detalles, marca=marca)
        obj.save()
        return redirect('/')

    return render(request, 'tienda/Aniadir.html',   {'formulario': formulario})


def edit(request, pk):
    print('hola')
    prod = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = productoForm(request.POST, instance=prod)

        if form.is_valid():
            form.save()
            return redirect('listado')

    form = productoForm(instance=prod)

    return render(request, 'tienda/editar.html', {'form': form})


def delete(request, pk):

    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('CRUD')

    return render(request, 'tienda/borrado.html', {'producto': producto})


def confirmaCompra(request):
    producto = Producto.objects.all()
    compra_form = CompraForm()

    return render(request, 'tienda/listado.html', {'productos': producto, 'compra_form': compra_form})


@transaction.atomic()
def checkout(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    compra_unidades = int(request.GET.get('unidades'))
    importe = 0

    if request.method == 'GET':
        compra_form = CompraForm(request.GET)

        if compra_form.is_valid():
            compra_unidades = compra_form.cleaned_data['unidades']
            precio_total = producto.precio * compra_unidades

            if compra_unidades <= 0:
                messages.warning(request, "Introduzca un número mayor o igual a 1.")
                return redirect('confirmaCompra')

            if compra_unidades > producto.unidades:
                messages.warning(request, "Se están intentando comprar más unidades de las disponibles.")
                return redirect('confirmaCompra')
        else:
            messages.error(request, "Error")
            return redirect('confirmaCompra')

    elif request.method == 'POST':
        importe = compra_unidades * producto.precio
        compra = Compra(producto=producto, unidades=compra_unidades, importe=importe)
        #compra.usuario = request.user
        compra.save()
        producto.unidades -= compra_unidades
        producto.save()
        messages.success(request, "Artículo: " + producto.nombre + " comprado con éxito.")
        return redirect('confirmaCompra')

    return render(request, 'tienda/checkout.html',
                  {'producto': producto, 'precio_total': precio_total, 'compra_unidades': compra_unidades,
                   'importe': importe})


def muestraInformes(request):
    informe = Compra.objects.all()
    if informe:
        return render(request, 'tienda/listado.html', {'informe': informe})
    else:
        messages.warning(request, "No hay compras registradas.")
        return render(request, 'tienda/listado.html')


def informes(request):

    return render(request, 'tienda/informes.html', {})


def comprasUsuario(request):
    if request.GET.get("user"):
        filtro_usuario = UsuarioForm(request.GET)

        if filtro_usuario.is_valid():
            user = filtro_usuario.cleaned_data.get('user')
            compras = Compra.objects.filter(user__username=user.username)

    else:
        filtro_usuario = UsuarioForm()
        compras = Compra.objects.all()

    return render(request, 'tienda/informes/comprasUsuario.html',
                  {'compras': compras, 'filtro_usuario': filtro_usuario})
