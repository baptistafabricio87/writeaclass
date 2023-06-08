from django.shortcuts import render

# Create your views here.
def index(request):
	template_name = 'index.html'
	return render(request, template_name)


def contato(request):
	template_name = 'contato.html'
	return render(request, template_name)


def sobre(request):
	template_name = 'sobre.html'
	return render(request, template_name)
