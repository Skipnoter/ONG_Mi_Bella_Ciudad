from django.shortcuts import render


# Create your views here.

'''Cargar noticias en la aplicación
Cargar fotos asociadas
Categorizar la noticia'''

from django.views.generic import ListView

from .models import Usuario


#conect = DATABASES.

class CargarNoticia(ListView):
    
    template_name = 'usuario/usuario.html'
    model = Usuario


class Login(ListView):
    template_name = 'usuario/login.html'
    model = Usuario