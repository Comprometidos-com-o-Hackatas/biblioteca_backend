from django.db import models
from core.biblioteca.models.livroPego import LivroPego
from datetime import datetime, timedelta

class Taxas(models.Model):
    class StatusTipo(models.IntegerChoices):
        PENDENTE = 1, 'Pendente'
        DEVOLVIDO = 2, 'Devolvido'

    livro = models.ForeignKey(LivroPego, on_delete=models.PROTECT, related_name="taxas")
    data_emprestado = models.DateField(auto_now=True)
    data_prometida = models.DateField(default=datetime.now() + timedelta(days=30))
    status = models.IntegerField(choices=StatusTipo.choices, default=StatusTipo.PENDENTE)

    @property
    def multa(self):
        dias_de_atraso = (datetime.now() - self.data_prometida).days()
        multa_atual = 0
        if dias_de_atraso > 0:
            for x in range(dias_de_atraso):
                multa_atual += dias_de_atraso
            return multa_atual
        else:
            return 0