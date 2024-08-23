from django.db import models
from core.usuario.models import Usuario as User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .livro import Livro

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    coment = models.TextField()
    nota = models.IntegerField()

@receiver(post_save, sender=Avaliacao)
def CalcularNota(instance, sender, **kwargs):
    avaliacoes = Avaliacao.objects.filter(livros=instance.livro)
    nota_geral = instance.nota

    for avaliacao in avaliacoes:
            nota_geral += avaliacao.nota 
        
    nota_geral = nota_geral / (len(avaliacoes) + 1)
    instance.livro.nota = nota_geral
    instance.livro.save()

    def __str__(self) -> str:
        return self.livro.titulo