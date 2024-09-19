from django.db import models
from core.usuario.models import Usuario as User
from .livro import Livro

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.livro.titulo