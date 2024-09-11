from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Motorista
from .forms import MotoristaForms
from django.contrib import messages

def listar_motorista(request):
    # Inicialize o formulário
    form = MotoristaForms()

    # Verifica se o método é POST para adição de motorista
    if request.method == 'POST':
        form = MotoristaForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Motorista adicionado com sucesso!')
            return redirect('listar_motorista')  # Redireciona para evitar duplicação de envio

    # Paginação dos motoristas
    motoristas = Motorista.objects.all().order_by('id')
    paginator = Paginator(motoristas, 10)  # Mostra 10 motoristas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Renderize a página com o formulário e o objeto da página paginada
    return render(request, 'motoristas/motorista.html', {"form": form, "page_obj": page_obj})
