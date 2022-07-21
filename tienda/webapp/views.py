from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from webapp.models import Producto


def inicio(request):
    nro_productos = Producto.objects.count()
    producto = Producto.objects.all()
    return render(request, 'inicio.html', {'nro': nro_productos, 'productos': producto})


def detalleproducto(request):
    return HttpResponse('Este será el detalle de cada producto')


