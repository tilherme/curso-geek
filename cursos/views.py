from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer

class CursoAPIView(APIView):
    """
    Api curso
    """
    def get(self, request):
        print(request.user)
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    

class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)