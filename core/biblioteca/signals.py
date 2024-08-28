from django.db.models.signals import post_save
from django.dispatch import receiver
from core.biblioteca.models import LivroPego, Taxas

@receiver(post_save, sender=LivroPego)
def CriarTaxa(sender, instance, created, **kwargs):
    # Verifica se foi Criado e Não alterado
    if created:
        Taxas.objects.create(livro=instance)