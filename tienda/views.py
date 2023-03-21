from django.shortcuts import render, redirect

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
