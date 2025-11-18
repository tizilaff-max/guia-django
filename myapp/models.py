from django.db import models

class Catalogo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    

    def __str__(self):
         return self.titulo


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=1)
    categoria = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre
    

