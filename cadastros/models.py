from django.db import models

# class Endereco(models.Model):
#     cep = models.CharField(max_length=8, default="00000-000")
#     bairro = models.CharField(max_length=150, default="Não especificado")
#     complemento = models.CharField(max_length=255, blank=True, null=True, default="Não especificado")
#     numero = models.CharField(max_length=10, default="S/N")
#     cidade = models.CharField(max_length=30, default="Não especificado")
#     uf = models.CharField(max_length=2, default="XX")
#     logradouro = models.CharField(max_length=255, default="Não especificado")
    
#     def __str__(self):
#         return f"Endereço com cep {self.cep} salvo com sucesso!"

class Cliente(models.Model):
    
    CLIENTE_CHOICES = [
        ("PF", "Pessoa Física"),
        ("PJ", "Pessoa Jurídica")
    ]
    
    nome = models.CharField(max_length=150, null=False, blank=False)
    cpfCnpj = models.CharField(max_length=14, null=False, blank=False)
    tipo = models.CharField(choices=CLIENTE_CHOICES, max_length=2, blank=False, null=False)
    # endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"Cliente {self.nome} salvo com sucesso!"