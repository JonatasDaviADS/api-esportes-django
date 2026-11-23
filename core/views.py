from decimal import Decimal, InvalidOperation
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiTypes,
)
from .models import ArtigoEsportivo
from .serializers import ArtigoEsportivoSerializer

TAG_CRUD = ['Artigos - CRUD']
TAG_FILTROS = ['Artigos - Filtros']


@extend_schema_view(
    list=extend_schema(tags=TAG_CRUD, summary='Listar todos os artigos'),
    create=extend_schema(tags=TAG_CRUD, summary='Cadastrar um artigo'),
    retrieve=extend_schema(tags=TAG_CRUD, summary='Buscar artigo por ID'),
    update=extend_schema(
        tags=TAG_CRUD, summary='Atualizar artigo (todos os campos)'),
    partial_update=extend_schema(
        tags=TAG_CRUD, summary='Atualizar artigo (só alguns campos)'),
    destroy=extend_schema(tags=TAG_CRUD, summary='Excluir artigo'),
)
class ArtigoEsportivoViewSet(viewsets.ModelViewSet):
    queryset = ArtigoEsportivo.objects.all()
    serializer_class = ArtigoEsportivoSerializer

    def _responder_lista(self, artigos):
        serializer = self.get_serializer(artigos, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=TAG_FILTROS,
        summary='Filtrar por modalidade',
        description='Busca parcial e sem diferenciar maiúsculas. Ex: Futebol, Corrida, Vôlei.',
        parameters=[OpenApiParameter(
            'modalidade', OpenApiTypes.STR, OpenApiParameter.PATH)],
        responses=ArtigoEsportivoSerializer(many=True),
    )
    @action(detail=False, methods=['get'], url_path=r'modalidade/(?P<modalidade>[^/.]+)')
    def por_modalidade(self, request, modalidade=None):
        artigos = self.queryset.filter(modalidade__icontains=modalidade)
        return self._responder_lista(artigos)

    @extend_schema(
        tags=TAG_FILTROS,
        summary='Filtrar por marca',
        description='Busca parcial e sem diferenciar maiúsculas. Ex: Nike, adidas.',   # 🆕
        parameters=[OpenApiParameter(
            'marca', OpenApiTypes.STR, OpenApiParameter.PATH)],
        responses=ArtigoEsportivoSerializer(many=True),
    )
    @action(detail=False, methods=['get'], url_path=r'marca/(?P<marca>[^/.]+)')
    def por_marca(self, request, marca=None):
        artigos = self.queryset.filter(marca__icontains=marca)
        return self._responder_lista(artigos)

    @extend_schema(
        tags=TAG_FILTROS,
        summary='Filtrar por cor',
        description='Busca parcial e sem diferenciar maiúsculas. Ex: Preta, Azul.',
        parameters=[OpenApiParameter(
            'cor', OpenApiTypes.STR, OpenApiParameter.PATH)],
        responses=ArtigoEsportivoSerializer(many=True),
    )
    @action(detail=False, methods=['get'], url_path=r'cor/(?P<cor>[^/.]+)')
    def por_cor(self, request, cor=None):
        artigos = self.queryset.filter(cor__icontains=cor)
        return self._responder_lista(artigos)

    @extend_schema(
        tags=TAG_FILTROS,
        summary='Filtrar por ano de lançamento',
        description='Ano exato, com 4 dígitos. Ex: 2025.',
        parameters=[OpenApiParameter(
            'ano', OpenApiTypes.INT, OpenApiParameter.PATH)],
        responses=ArtigoEsportivoSerializer(many=True),
    )
    @action(detail=False, methods=['get'], url_path=r'ano/(?P<ano>[0-9]{4})')
    def por_ano(self, request, ano=None):
        artigos = self.queryset.filter(ano=ano)
        return self._responder_lista(artigos)

    @extend_schema(
        tags=TAG_FILTROS,
        summary='Filtrar por faixa de preço',
        description='Retorna artigos com valor entre min e max (inclusive), do mais barato ao mais caro.',
        parameters=[
            OpenApiParameter('min', OpenApiTypes.DECIMAL, OpenApiParameter.QUERY, required=True,
                             description='Valor mínimo. Ex: 100'),
            OpenApiParameter('max', OpenApiTypes.DECIMAL, OpenApiParameter.QUERY, required=True,
                             description='Valor máximo. Ex: 500'),
        ],
        responses=ArtigoEsportivoSerializer(many=True),
    )
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
