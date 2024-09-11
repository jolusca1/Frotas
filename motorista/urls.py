from django.urls import path
from .views import listar_motorista

urlpatterns = [
    path('motoristas/', listar_motorista, name='listar_motorista')
    # path('motoristas/cadastrar/', cadastrar_motorista, name='cadastrar_motorista'), # Exemplo de outra URL, se necessário
]
