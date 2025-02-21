from django.db import models

class Formulario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    comentario = models.TextField()

    def __str__(self):
        return self.nome
