from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dt_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')

    class Meta:
        verbose_name='Pessoa'
        verbose_name_plural='Pessoas'
        ordering

    def __str__(self):
        return self.nome
