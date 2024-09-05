from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Motorista
from .forms import MotoristaForms
from django.contrib import messages

def listar_motorista(request):
    motoristas = Motorista.objects.all()
    paginator = Paginator(motoristas, 10)  # Mostra 10 motoristas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Inicialize o formulário
    form = MotoristaForms()
    
    if request.method == 'POST':
        form = MotoristaForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Adicionado com sucesso!')
            return redirect('listar_motorista')  # Redireciona para a mesma página para evitar duplicação de envio

    # Renderize a página com o formulário e o objeto da página paginada
    return render(request, 'motoristas/motorista.html', {"page_obj": page_obj, "form": form})
