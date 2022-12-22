from django.conf import settings
#from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from aplications.noticia.views import PaginaInicio
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaginaInicio.as_view(), name='inicio'),
    path('', include('aplications.usuario.urls')),
    path('', include('aplications.noticia.urls')),
    path('', include('aplications.categorias.urls')),
    path('', include('aplications.comentario.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns +=[
#    re_path(r'^media/(?P<path>.*)$',serve,{
#        'document_root':settings.MEDIA_ROOT,
#        })
#]
