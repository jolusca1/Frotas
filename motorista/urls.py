from django.urls import path
from .views import listar_motorista

urlpatterns = [
    path('motoristas', listar_motorista)
]