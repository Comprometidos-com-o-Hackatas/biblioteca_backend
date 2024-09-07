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

    def __str__(self) -> str:
        return self.livro.titulo



@receiver(post_save, sender=Avaliacao)
def CalcularNota(instance, sender, **kwargs):
    avaliacoes = Avaliacao.objects.filter(livro=instance.livro)
    
    if avaliacoes.exists():
        nota_geral = sum(avaliacao.nota for avaliacao in avaliacoes) / avaliacoes.count()
    else:
        nota_geral = instance.nota
    
    instance.livro.nota = nota_geral
    instance.livro.save()