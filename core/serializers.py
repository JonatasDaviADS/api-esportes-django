from rest_framework import serializers
from .models import ArtigoEsportivo


class ArtigoEsportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtigoEsportivo
        fields = '__all__'

    def validate_valor(self, valor):
        if valor <= 0:
            raise serializers.ValidationError(
                "O valor deve ser maior que zero.")
        return valor

    def validate_ano(self, ano):
        if ano < 1900 or ano > 2100:
            raise serializers.ValidationError(
                'Informe um ano entre 1900 e 2100.')
        return ano
