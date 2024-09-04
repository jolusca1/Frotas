from django.shortcuts import render, redirect
from .models import Motorista
from .forms import MotoristaForms
from django.contrib import messages


def listar_motorista(request):
    motoristas = Motorista.objects.all()
    return render(request, 'motoristas/motorista.html', {"motoristas": motoristas})

def cadastrar_motorista(request):
    
    form = MotoristaForms
    if request.method == 'POST':
        form = MotoristaForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Adicionado com sucesso!')
            return redirect('listar_motorista')
    return render(request, 'motoristas/cadastrar_motorista.html', {'form': form})