from django.shortcuts import render, redirect
# from .models import Cliente

# from .forms import ClienteForm


def index(request):
    return render(request, 'home/home.html')