from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)

class Cliente(models.Model):
    
    CLIENTE_CHOICES = [
        ("PF", "Pessoa Física"),
        ("PJ", "Pessoa Jurídica")
    ]
    
    nome = models.CharField(max_length=150, null=False, blank=False)
    cpfCnpj = models.CharField(max_length=14, null=False, blank=False)
    tipo = models.CharField(choices=CLIENTE_CHOICES, max_length=2, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)