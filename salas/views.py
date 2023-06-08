from django.shortcuts import render

from salas.models import Sala, Aula, Comentario

# Create your views here.
def listar_salas(request):
	template_name = 'salas.html'
	object_list = Sala.objects.order_by('-criado_em')
	paginator = Paginator(object_list, 3)  # 3 objects in each page
    page = request.GET.get('page')
    
    try:
        salas_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        salas_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        salas_list = paginator.page(paginator.num_pages)
    
    return render(
        request, template_name, {'page': page, 'salas_list': salas_list}
    )


def listar_aulas(request):
	template_name = 'aulas.html'
    object_list = Aula.objects.filter(publicado=True).order_by('-criado_em')
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    
    try:
        aulas_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        aulas_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        aulas_list = paginator.page(paginator.num_pages)
    
    return render(
        request, template_name, {'page': page, 'aulas_list': aulas_list}
    )


def detalhe_da_aula(request, slug):
    template_name = 'detalhe_da_aula.html'
    aula = get_object_or_404(Aula, slug=slug)
    comentario = aula.comentarios.filter(active=True)
    novo_comentario = True
    
    # Comment posted
    if request.method == 'POST':
        form_comentario = CommentForm(data=request.POST)
        if form_comentario.is_valid():
            # Create Comment object but don't save to database yet
            novo_comentario = form_comentario.save(commit=False)
            # Assign the current post to the comment
            novo_comentario.aula = aula
            # Save the comment to the database
            novo_comentario.save()
    else:
        form_comentario = CommentForm()
    
    return render(
        request,
        template_name,
        {
            'aula': aula,
            'comentarios': comentarios,
            'novo_comentario': novo_comentario,
            'form_comentario': form_comentario,
        },
    )


def buscar(request):
    aulas = Aula.objects.filter(publicado=True).order_by('-criado_em')
    if 'buscar' in request.GET:
        buscar_nome = request.GET['search']
        if search:
            aulas = lista_aulas.filter(buscar_nome)
            
    data = {'aulas' : lista_de_aulas}
        
    return render(request, 'salas.html', data)