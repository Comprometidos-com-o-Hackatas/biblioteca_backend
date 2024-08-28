from rest_framework import serializers
from core.biblioteca.models import Taxas

class TaxaSerializer(serializers.ModelSerializer):
    livro, data_emprestado, data_prometida, multa = serializers.ReadOnlyField()

    class Meta:
        model = Taxas
        fields = ['status']