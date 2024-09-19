from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])

        return super().create(validate_data)