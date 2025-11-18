from django.shortcuts import render
from .models import Catalogo, Producto
from django.http import HttpResponse


def inicio(request):
    categorias = Catalogo.objects.all()
    return render(request, 'myapp/inicio.html', {'categorias': categorias})
def categorias(request):
    return render(request, 'myapp/categorias.html')


def productos_por_categoria(request, nombre_categoria):
    try:
        categoria = Catalogo.objects.get(titulo=nombre_categoria)
    except Catalogo.DoesNotExist:
        return HttpResponse("No existe esa categoría en la base.")

    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'myapp/productos_por_categoria.html', {'categoria': categoria, 'productos': productos})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'myapp/lista_productos.html', {'productos': productos})



def crear_catalogo(request, titulo, contenido):
    nuevo = Catalogo.objects.create(
        titulo=titulo,
        contenido=contenido
    )
    return HttpResponse(f"Catalogo creado: {nuevo.titulo}")


def crear_producto(request, nombre, precio, id_categoria):
    try:
        categoria = Catalogo.objects.get(id=id_categoria)
    except Catalogo.DoesNotExist:
        return HttpResponse("La categoria no existe, no se puede crear el producto.")

    prod = Producto.objects.create(
        nombre=nombre,
        precio=precio,
        categoria=categoria
    )
    return HttpResponse(f"Producto creado: {prod.nombre}")
