from django.shortcuts import render, redirect, get_object_or_404
from .forms import productoForm
from tienda.models import Producto


# Create your views here.


def welcome(request):
    return render(request,'tienda/index.html', {})


def crud(request):
    prod = Producto.objects.all()

    return render(request, 'tienda/CRUD.html', {'prod':prod})

def creaProducto(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        modelo = request.POST['modelo']
        unidades = request.POST['unidades']
        precio = request.POST['precio']
        detalles = request.POST['detalles']
        marca = request.POST['marca']
        obj = Producto.objects.create(nombre=nombre, modelo=modelo,
                                      unidades=unidades, precio=precio,
                                      detalles=detalles, marca=marca)
        obj.save()
        return redirect('/')


def muestraProducto(request):

    prod = Producto.objects.all()
    # if request.method == 'GET':
    #
    #     producto =

    return render(request, 'tienda/listado.html', {'prod': prod})


def edit(request, id):
    object = Producto.objects.get(id=id)
    return render(request, 'editar.html', {'object': object})


def delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('CRUD')
    return render(request, 'tienda/borrado.html', {'producto': producto})


def update(request, id):
    object = Producto.objects.get(id=id)
    form = productoForm(request.POST, instance=object)
    if form.is_valid:
        form.save()
        object = Producto.objects.all()
        return redirect('muestraProducto')


