from django.shortcuts import render
from .models import Catalogo, Producto

def inicio(request):
    categorias = Catalogo.objects.all()
    return render(request, 'myapp/inicio.html', {'categorias': categorias})
def categorias(request):
    return render(request, 'myapp/categorias.html')


def productos_por_categoria(request, nombre_categoria):
    categoria = Catalogo.objects.get(titulo = nombre_categoria)
    productos = Producto.objects.filter(categoria = categoria)
    return render(request, 'myapp/productos_por_categoria.html', {'categoria': categoria, 'productos': productos})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'myapp/lista_productos.html', {'productos': productos})