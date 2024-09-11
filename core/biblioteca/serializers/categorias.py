from ..models import Categoria
from rest_framework import serializers

class CategoriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields: list[str] = [ "id", "descricao" ]

class CategoriaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields: list[str] = [ "id", "   descricao" ]