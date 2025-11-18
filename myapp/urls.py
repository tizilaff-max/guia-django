from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('productos/<str:nombre_categoria>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('crear_catalogo/<str:titulo>/<str:contenido>/', views.crear_catalogo, name='crear_catalogo'),
    path('crear_producto/<str:nombre>/<str:precio>/<int:id_categoria>/', views.crear_producto, name='crear_producto'),
]