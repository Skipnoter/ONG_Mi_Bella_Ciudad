from time import timezone
from datetime import datetime, date
from django.db import models

# Create your models here.
from aplications.usuario.models import Usuario

# Create your models here.

class Comentarios(models.Model):

   # id_usuario = models.ForeignKey(Usuarios , on_delete=models.CASCADE)
    #fecha_comentario = 
    #hora_comentario =
    comentarios = models.CharField('Comentario', max_length=2000)
    #noticia =

    #cant_likes =

    def __str__(self) :
        return str(self.id) + '-' +  self.comentarios