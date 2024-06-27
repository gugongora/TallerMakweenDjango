from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, ItemCarrito

from datetime import datetime

# Create your views here.

def index(request):
    context={}
    return render(request, 'taller/index.html', context)

def footer(request):
    context={}
    return render(request, 'taller/footer.html', context)

def navbar(request):
    context={}
    return render(request, 'taller/navbar.html', context)

def mantencion(request):
    context={}
    return render(request, 'taller/mantencion.html', context)

def reparacion(request):
    context={}
    return render(request, 'taller/reparacion.html', context)

def refacciones(request):
    context={}
    return render(request, 'taller/refacciones.html', context)

def trabajos(request):
    context={}
    return render(request, 'taller/trabajos.html', context)

def equipo(request):
    context={}
    return render(request, 'taller/equipo.html', context)

def contacto(request):
    context={}
    return render(request, 'taller/contacto.html', context)

def nuevologin(request):
    context={}
    return render(request, 'taller/nuevologin.html', context)

def agregar_al_carrito(request, producto_id):
    # Intentar obtener el carrito de la sesión, o crear uno nuevo si no existe
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito, created = Carrito.objects.get_or_create(id=carrito_id)
    else:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id

    # Obtener el producto usando pro_id
    producto = get_object_or_404(Producto, pro_id=producto_id)

    # Agregar el producto al carrito o incrementar la cantidad si ya existe
    item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item_carrito.cantidad += 1
    item_carrito.save()

    # Redirigir a la vista del carrito para evitar la repetición de acciones
    return redirect('ver_carrito')

def obtener_carrito(request):

    
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        try:
            return Carrito.objects.get(id=carrito_id)
        except Carrito.DoesNotExist:
            return None
    else:
        return None

def vaciar_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        carrito.items.all().delete()
        carrito.delete()
        request.session['carrito_id'] = None
    return redirect('ver_carrito')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'taller/product_list.html', {'productos': productos})


def ver_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        try:
            carrito = Carrito.objects.get(id=carrito_id)
            items = carrito.items.all()
        except Carrito.DoesNotExist:
            carrito = None
            items = []
    else:
        carrito = None
        items = []

    return render(request, 'taller/ver_carrito.html', {'carrito': carrito, 'items': items})


def eliminar_del_carrito(request, item_id):
    # Obtener el item del carrito y eliminarlo
    item = get_object_or_404(ItemCarrito, id=item_id)
    carrito = item.carrito
    item.delete()

    # Verificar si el carrito está vacío y eliminarlo si es necesario
    if not carrito.items.exists():
        carrito.delete()
        request.session['carrito_id'] = None

    # Redirigir a la vista del carrito para evitar la repetición de acciones
    return redirect('ver_carrito')