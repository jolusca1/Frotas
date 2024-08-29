from django.contrib import admin
from cadastros.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpfCnpj', 'tipo', 'endereco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    
admin.site.register(Cliente, Clientes)