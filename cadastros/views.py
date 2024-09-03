from django.shortcuts import render, redirect
from .models import Cliente

from .forms import ClienteForm


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'clientes': clientes})