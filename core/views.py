from django.shortcuts import render

# Create your views here.
def index(request):
	template_name = 'index.html'
	return render(request, template_name)


def salas(request):
	template_name = 'salas.html'
	return render(request, template_name)


def contato(request):
	template_name = 'contato.html'
	return render(request, template_name)


def sobre(request):
	template_name = 'sobre.html'
	return render(request, template_name)


def login(request):
	template_name = 'login.html'
	return render(request, template_name)


def cadastro(request):
	template_name ='cadastro.html'
	return render(request, template_name)
