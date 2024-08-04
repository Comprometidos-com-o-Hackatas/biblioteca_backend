from django.db import models
from core.usuario.models import Usuario as User
from .livro import Livro

class LivroPego(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_pego = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.usuario.email
    
    def LivroIndisponivel(self):
        self.livro.disponivel = not self.livro.disponivel
        self.livro.save()

    def save(self, *args, **kwargs):
        self.LivroIndisponivel()
        return super().save(*args, **kwargs)