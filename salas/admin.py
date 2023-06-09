from django.contrib import admin
from salas.models import Sala, Aula, Comentario

# Register your models here.

class AulaAdmin(admin.ModelAdmin):
    '''
        Admin View for Aula
    '''
    list_display = ('titulo', 'categoria', 'criado_em')
    list_filter = ('criado_em', 'categoria', 'publicado')
    search_fields = ('titulo', 'categoria', 'conteudo')
    prepopulated_fields  =  {"slug" :  ('autor', 'titulo',)}

admin.site.register(Aula, AulaAdmin)

class SalaAdmin(admin.ModelAdmin):
    '''
        Admin View for Sala
    '''
    list_display = ('nome', 'aula', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome',)

admin.site.register(Sala, SalaAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    '''
        Admin View for Comentario
    '''
    list_display = ('aula', 'nome', 'email')
    list_filter = ('aula', 'criado_em')
    search_fields = ('aula', 'criado_em', 'email')

admin.site.register(Comentario, ComentarioAdmin)