from django.shortcuts import render, redirect
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




def crear_catalogo_view(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        contenido = request.POST.get("contenido")

        Catalogo.objects.create(titulo=titulo, contenido=contenido)
        return redirect('inicio')

    return render(request, "myapp/crear_catalogo.html")


def crear_producto_view(request):
    categorias = Catalogo.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        categoria_id = request.POST.get("categoria")

        categoria = Catalogo.objects.get(id=categoria_id)
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            categoria=categoria
        )
        return redirect('lista_productos')

    return render(request, "myapp/crear_producto.html", {"categorias": categorias})
