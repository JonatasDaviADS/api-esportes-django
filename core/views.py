from rest_framework import viewsets
from .models import ArtigoEsportivo
from .serializers import ArtigoEsportivoSerializer


class ArtigoEsportivoViewSet(viewsets.ModelViewSet):
    queryset = ArtigoEsportivo.objects.all()
    serializer_class = ArtigoEsportivoSerializer
