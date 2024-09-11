from django.db import models
from core.usuario.models import Usuario
from .livro import Livro

class Familia(models.Model):
    nome = models.CharField(max_length=80, null=False, default='+')
    Usuario = models.ManyToManyField(Usuario, related_name='+')

    def __str__(self) -> str:
        return self.nome