from django.db import models

#tabela do banco
class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    ano = models.IntegerField()