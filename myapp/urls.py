from django.urls import path
from . import views
from myapp.views import inicio, categorias


urlpatterns = [
    path('', inicio, name='inicio'),
    path('categorias/', categorias, name='categorias'),
    path('productos/<str:nombre_categoria>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('productos/', views.lista_productos, name='lista_productos'),

]