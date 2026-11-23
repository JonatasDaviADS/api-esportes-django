from decimal import Decimal, InvalidOperation
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ArtigoEsportivo
from .serializers import ArtigoEsportivoSerializer


class ArtigoEsportivoViewSet(viewsets.ModelViewSet):
    queryset = ArtigoEsportivo.objects.all()
    serializer_class = ArtigoEsportivoSerializer

    def _responder_lista(self, artigos):
        serializer = self.get_serializer(artigos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'modalidade/(?P<modalidade>[^/.]+)')
    def por_modalidade(self, request, modalidade=None):
        artigos = self.queryset.filter(modalidade__icontains=modalidade)
        return self._responder_lista(artigos)

    @action(detail=False, methods=['get'], url_path=r'marca/(?P<marca>[^/.]+)')
    def por_marca(self, request, marca=None):
        artigos = self.queryset.filter(marca__icontains=marca)
        return self._responder_lista(artigos)

    @action(detail=False, methods=['get'], url_path=r'cor/(?P<cor>[^/.]+)')
    def por_cor(self, request, cor=None):
        artigos = self.queryset.filter(cor__icontains=cor)
        return self._responder_lista(artigos)

    @action(detail=False, methods=['get'], url_path=r'ano/(?P<ano>[^/.]+)')
    def por_ano(self, request, ano=None):
        artigos = self.queryset.filter(ano=ano)
        return self._responder_lista(artigos)

    @action(detail=False, methods=['get'], url_path=r'faixa-preco')
    def por_faixa_preco(self, request):
        minimo = request.query_params.get('min')
        maximo = request.query_params.get('max')

        if minimo is None or maximo is None:
            return Response(
                {'erro': 'informe os parâmetros min e max. Ex: ?min=100&max=500'},
                status=status.HTTP_400_BAD_REQUEST,

            )

        try:
            minimo = Decimal(minimo)
            maximo = Decimal(maximo)
        except InvalidOperation:
            return Response(
                {'erro': 'min e max devem ser números. Use ponto para centavos.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if minimo > maximo:
            return Response(
                {'erro': 'O valor de min não pode ser maior que max.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        artigos = self.queryset.filter(
            valor__gte=minimo, valor__lte=maximo).order_by('valor')
        return self._responder_lista(artigos)
