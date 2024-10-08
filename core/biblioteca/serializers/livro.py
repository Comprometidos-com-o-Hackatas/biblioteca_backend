from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import Livro
from core.uploader.serializers import ImageSerializer
from core.uploader.models import Image

class LivroListSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autores', 'capa', 'capa_attachment_key', 'disponivel', 'categoria', 'generos', 'descricao', 'nota', 'data_lancamento']
        depth = 1

class LivroDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1