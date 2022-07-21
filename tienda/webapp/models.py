from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=255)

    """def __str__(self):
        return f'CategoriaProducto {self.id}: {self.categoria}'"""

class Producto(models.Model):
    nombreproducto = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True)

    """def __str__(self):
        return f'Producto {self.id}: {self.nombreproducto} {self.precio}'"""
