from django.shortcuts import render
from .models import Articulo


def home (request):
    articulos = Articulo.objects.all()
    context = {
        'articulos': articulos
    }
    return render(request,'home.html',context)


def catalogo (request):
    articulos = Articulo.objects.all()
    context = {
        'articulos': articulos
    }
    return render(request,'catalogo.html',context)


def detalle (request, key):
    articulo = Articulo.objects.get(pk=key)
    context = {
        'articulo': articulo
    }
    return render(request,'detalle.html',context)


def contacto (request):
    return render(request,'contacto.html', {})
