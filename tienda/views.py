from django.shortcuts import render, redirect, get_object_or_404
from .forms import productoForm
from tienda.models import Producto, Marca


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


def muestraProducto(request):

    prod = Producto.objects.all()
    # if request.method == 'GET':
    #
    #     producto =

    return render(request, 'tienda/listado.html', {'prod': prod})


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


