from django.contrib import admin
from . import models

admin.site.register(models.Autores)
admin.site.register(models.Categoria)
admin.site.register(models.Livro)
admin.site.register(models.Avaliacao)
admin.site.register(models.Generos)
admin.site.register(models.Favorito)
