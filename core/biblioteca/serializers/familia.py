from core.biblioteca.models.familia import Familia
from core.usuario.models import Usuario
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class FamiliaSerializer(ModelSerializer):
    # Definindo o campo ManyToMany como PrimaryKeyRelatedField para aceitar IDs de usuários
    Usuario = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.all())
    
    class Meta:
        model = Familia
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        usuarios_data = validated_data.pop('Usuario', [])
        familia = Familia.objects.create(**validated_data)
        familia.Usuario.set(usuarios_data)

        return familia

    def update(self, instance, validated_data):
        usuarios_data = validated_data.pop('Usuario', [])

        instance = super().update(instance, validated_data)

        instance.Usuario.set(usuarios_data)

        return instance
