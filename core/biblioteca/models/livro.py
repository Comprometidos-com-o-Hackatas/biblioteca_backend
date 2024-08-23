from django.db import models
from core.uploader.models import Image
from .categoria import Categoria
from .genero import Generos
from .autores import Autores

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    capa = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='+', default=None, blank=True, null=True)
    descricao = models.TextField()
    data_lancamento = models.DateField()
    disponivel = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    generos = models.ManyToManyField(Generos)
    autores = models.ManyToManyField(Autores)
    nota = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self) -> str:
        return self.titulo


    
