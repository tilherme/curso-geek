from rest_framework import serializers

from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        #extra_kwargs só vai mostrar no cadastro
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'atualizacao',
            'ativo',
        )

class CursoSerializer(serializers.ModelSerializer):
    # Nested relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field 
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True, 
    #     read_only=True,
    #     view_name='avaliacao-detail')
   # Primary key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'atualizacao',
            'ativo',
            'avaliacoes'
        )