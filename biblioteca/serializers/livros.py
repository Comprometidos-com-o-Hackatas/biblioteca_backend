from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import Livros
from uploader.serializers import ImageSerializer
from uploader.models import Image

class LivrosDetailSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Livros
        fields = "__all__"
        depth = 2

class LivrosListSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:
        model = Livros
        fields: list[str] = ['id', 'capa', 'disponivel', 'titulo', 'genero', 'categoria']

