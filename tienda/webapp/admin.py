from django.contrib import admin

# Register your models here.
from webapp.models import Producto, CategoriaProducto

admin.site.register(CategoriaProducto)
admin.site.register(Producto)

