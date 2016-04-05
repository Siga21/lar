from django.contrib import admin
from libros.models import autores, lectores, titulos

# Register your models here.

admin.site.register(autores)
admin.site.register(lectores)
admin.site.register(titulos)

