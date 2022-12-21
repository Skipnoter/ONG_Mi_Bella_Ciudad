from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

# Create your views here.

from django.views.generic import ListView

from .models import Noticia
from .forms import FormularioNoticias


#conect = DATABASES.

class ListarNoticias(ListView):
    
    template_name = 'noticia/noticias_varias.html'
    model = Noticia




#class Login(ListView):
 #   template_name = 'usuario/login.html'
  #  model = Noticia


class PaginaInicio(TemplateView):
    template_name = "base.html"



class NoticiasCreateView(CreateView):
    template_name = 'noticia/noticia.html'
    model = Noticia
    form_class = FormularioNoticias


    def get_success_url(self):
        print(self)
        return reverse_lazy('exito')


    def form_valid(self, form):

        if( form.is_valid()):
            noticia = Noticia(            
                categorias= form.data.get('categoria'),
                titulo= form.data.get('titulo'),
                subtitulo_detalles= form.data.get('subtitulo_detalles'),
                texto= form.data.get('texto')
                )
        
        noticia.save()
        print('guardado')
        return super(NoticiasCreateView, self).form_valid(form)

   