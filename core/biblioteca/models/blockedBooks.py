from django.db import models
from core.usuario.models import Usuario
from .livro import Livro
from .categoria import Categoria
from .genero import Generos

class BlockedLivros(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Livro = models.ManyToManyField(Livro, related_name='blocked_livros')
    Categoria = models.ManyToManyField(Categoria, related_name='blocked_livros')
    Generos = models.ManyToManyField(Generos, related_name='blocked_livros')