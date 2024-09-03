from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=150, blank=False, null=False)
    matricula = models.CharField(max_length=20, blank=False, null=False)
    cnh = models.CharField(max_length=20, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    data_emissao = models.DateField(blank=False)
    data_validade = models.DateField(blank=False)
    categoria_cnh = models.CharField(max_length=11, blank=False, null=False)