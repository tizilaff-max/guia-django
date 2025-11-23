from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('productos/<str:nombre_categoria>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('crear_catalogo/', views.crear_catalogo_view, name='crear_catalogo_view'),
    path('crear_producto/', views.crear_producto_view, name='crear_producto_view'),
]
