from django.db import models

class Notas(models.Model):
    titulo = models.CharField(max_length=30)
    nota = models.CharField(max_length=200)
    Fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo