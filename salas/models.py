from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sala(models.Model):
	nome_sala = models.CharField(max_length=50, verbose_name='Sala')
    aulas = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='lista_aulas' verbose_name='Lista de Aulas')
	criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criada em')

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ['-criado_em']

    def __str__(self):
        return f'Sala: {self.nome_sala}'


class Aula(models.Model):
    titulo = models.CharField(max_length=100, unique=True, verbose_name='Titulo')
    slug = models.SlugField(max_length=100, unique=True)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='autor_aula', verbose_name='Autor'
    )
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name)
    categoria = models.CharField(verbose_name='Categoria', max_length=50)
    conteudo = models.TextField(verbose_name='Conteúdo')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    publicado = models.BooleanField(default=False, verbose_name='Publicado')

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"
        ordering = ['-criado_em']

    def __str__(self):
        return f'Titulo: {self.title}'


class Comentario(models.Model):
    aula = models.ForeignKey(
        Aula, on_delete=models.CASCADE, related_name='comentarios', verbose_name='Comentario Aula'
    )
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    criado_em = models.DateTimeField(
    	auto_now_add=True, verbose_name='Criado em'
    )
    ativo = models.BooleanField(default=False, verbose_name='Ativo')

    class Meta:
    	verbose_name = 'Comentario'
    	verbose_name_plural = 'Comentarios'
        ordering = ['criado_em']

    def __str__(self):
        return f'Comentario: {self.comentario} by {self.nome}'

