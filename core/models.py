from django.db import models


class ArtigoEsportivo(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    ano = models.IntegerField()
    modalidade = models.CharField(max_length=50)

    class Meta:
        db_table = 'artigos_esportivos'
        ordering = ['id']
        verbose_name = 'Artigo Esportivo'
        verbose_name_plural = 'Artigos Esportivos'

    def __str__(self):
        return f'{self.nome} - {self.marca}'
