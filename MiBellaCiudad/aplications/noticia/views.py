from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView

from .models import Noticia


#conect = DATABASES.

class ListarNoticias(ListView):
    
    template_name = 'noticia/noticias_varias.html'
    model = Noticia


#class Login(ListView):
 #   template_name = 'usuario/login.html'
  #  model = Noticia