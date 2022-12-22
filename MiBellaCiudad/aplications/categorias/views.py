from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

# Create your views here.

from django.views.generic import ListView

from .models import Categorias
from .forms import FormularioCategorias


#conect = DATABASES.

class CrearCategoria(ListView):
    
    template_name = 'categoria/categorias.html'
    model = Categorias



class PaginaInicio(TemplateView):
    template_name = "base.html"



class CategoriaCreateView(CreateView):
    template_name = 'categorias/categorias.html'
    model = Categorias
    form_class = FormularioCategorias

    
    def get_success_url(self):
        print(self)
        return reverse('exito')

    '''
    def form_valid(self, form):

        if( form.is_valid()):
            categoria = Categorias(            
                categorias= form.data.get('categoria'),
                )
        
        categoria.save()
        print('guardado')
        return super(CategoriaCreateView, self).form_valid(form)
        '''
