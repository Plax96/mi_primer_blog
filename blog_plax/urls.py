from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.publicacion_detalle, name='publicacion_detalle'),
    url(r'^post/nueva/$', views.publicacion_nueva, name='publicacion_nueva'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.publicacion_editar, name='publicacion_editar'),
    url(r'^post/publish/(?P<pk>\d+)/$', views.publicacion_publicar, name='publicacion_publicar'),
    url(r'^drafts/$', views.publicacion_lista_borrador, name='publicacion_lista_borrador'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.publicar_remover, name='publicar_remover'),


]
