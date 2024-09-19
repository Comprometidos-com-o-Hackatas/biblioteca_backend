from core.biblioteca.models.blockedBooks import BlockedLivros
from rest_framework.serializers import ModelSerializer

class BlockedBooksSerializer(ModelSerializer):
    class Meta:
        model = BlockedLivros
        fields = "__all__"
        depth = 1