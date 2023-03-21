from django.shortcuts import render, redirect
from .forms import productoForm
from tienda.models import Producto


# Create your views here.


def welcome(request):
    return render(request,'tienda/index.html', {})


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
    return render(request, 'muestraProducto.html', {'prod': prod})


def edit(request, id):
    object = Producto.objects.get(id=id)
    return render(request, 'editar.html', {'object': object})


def update(request, id):
    object = Producto.objects.get(id=id)
    form = productoForm(request.POST, instance=object)
    if form.is_valid:
        form.save()
        object = Producto.objects.all()
        return redirect('muestraProducto')