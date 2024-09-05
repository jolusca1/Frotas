from django.urls import path
from .views import listar_motorista

urlpatterns = [
    path('motoristas', listar_motorista, name='listar_motorista')
    # path('cadastrar_motorista', cadastrar_motorista, name='cadastrar_motorista')
]