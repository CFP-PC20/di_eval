from django.shortcuts import render
from .models import Articulo


def home(request):
    articulos = Articulo.objects.all()
    context = {
        'articulos': articulos
    }
    return render(request,'home.html',context)


def product_index(request):
    articulos = Articulo.objects.all()
    context = {
        'articulos': articulos
    }
    return render(request,'product_index.html',context)


def product_detail(request,key):
    articulo = Articulo.objects.get(pk=key)
    context={
        'articulo': articulo
    }
    return render(request,'product_detail.html',context)