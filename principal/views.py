from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
	entradas = Entradas.objects.all().order_by('-id')
	return render(request, 'index.html', {'entradas':entradas})

def insertar_entrada(request):
	if request.method == 'POST':
		entrada_form = EntradasForm(request.POST)
		if entrada_form.is_valid():
			entrada_form.save()
			return redirect('/')
	else:
		entrada_form = EntradasForm()

	return render(request, 'insertar_entrada.html', {'entrada_form':entrada_form})