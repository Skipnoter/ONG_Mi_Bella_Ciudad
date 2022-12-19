from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(models.Model):

    tipo = models.BooleanField('admin')
    nombres = models.CharField('nombres', max_length=50)
    apellidos = models.CharField('apellidos', max_length=50)
    celular = models.IntegerField('celular')
    fecha_de_nacimiento = models.DateField()
    e_mail = models.EmailField()
    password = models.CharField(max_length=20)
    fecha_hora_registro = models.DateTimeField(auto_now_add=True)
    



    def __str__(self):
        return   self.nombres