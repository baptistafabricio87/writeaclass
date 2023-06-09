from django.urls import path
from salas.views import listar_salas, listar_aulas


urlpatterns = [
	path('', listar_salas, name='salas'),
	path('aulas/', listar_aulas, name='aulas'),
]