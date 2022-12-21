from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(models.Model):
    phone_message = 'Phone number must be entered in the format: 05999999999'
    phone_regex = RegexValidator( regex=r'\d{9}$', message=phone_message )
    
    tipo = models.BooleanField('admin')
    nombres = models.CharField('nombres', max_length=50)
    apellidos = models.CharField('apellidos', max_length=50)
    celular =  models.CharField( validators=[phone_regex], max_length=60,null=True, blank=True )
    fecha_de_nacimiento = models.DateField()
    e_mail = models.EmailField()
    password = models.CharField(max_length=20)
    fecha_hora_registro = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return   self.nombres


