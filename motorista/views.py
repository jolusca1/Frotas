from django.shortcuts import render
from .models import Motorista

def listar_motorista(request):
    motoristas = Motorista.objects.all()
    return render(request, 'motoristas/motorista.html', {"motoristas": motoristas})