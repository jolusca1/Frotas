from django.contrib import admin
from .models import Motorista

class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    
    
admin.site.register(Motorista, MotoristaAdmin)