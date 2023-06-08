from django.urls import path
from salas.views import 

urlpatterns = [
	path('salas/', salas, name='salas'),
	path('aulas/', aulas, name='aulas'),
]