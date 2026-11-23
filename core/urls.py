from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtigoEsportivoViewSet

router = DefaultRouter()
router.register('artigos', ArtigoEsportivoViewSet, basename='artigo')

urlpatterns = [
    path('', include(router.urls)),
]
