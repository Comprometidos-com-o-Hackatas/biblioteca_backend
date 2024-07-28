from django.db import models
from django.contrib.auth.models import User
from .livros import Livros
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

class LivroPego(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE, verbose_name='livros')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuario')
    data_pego = models.DateField(auto_now=True)

@receiver(post_save, sender=LivroPego)
def DisponibilidadeLivro(sender, instance, **kwargs):
    instance.livro.disponivel = False
    instance.save()

@receiver(post_delete, sender=LivroPego)
def EntregueLivro(sender, instance, **kwargs):
    instance.livro.disponivel = True
    instance.save()

    