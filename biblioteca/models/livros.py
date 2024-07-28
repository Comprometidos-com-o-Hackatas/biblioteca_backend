from django.db import models
from .categoria import Categoria
from .autores import Autores
from .genero import Generos
from uploader.models.image import Image

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    capa = models.ForeignKey(Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,)
    lancamento = models.DateField()
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='categoria')
    autores = models.ManyToManyField(Autores)
    generos = models.ManyToManyField(Generos)


    def __str__(self):
        return self.titulo

