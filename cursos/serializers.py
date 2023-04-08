from rest_framework import serializers
from django.db.models import Avg
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

    def validate_avaliacao(self, value):
        if value in range(1,6):
            return value
        else:
            raise serializers.ValidationError('A avaliação não pode receber essa nota')
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
    media_avaliacoes = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'atualizacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        print('@@@@@@ 1')

        if media is None:
            return 0
        return round(media * 2) / 2
    