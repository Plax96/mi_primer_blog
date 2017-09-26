from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>\d+)/$', views.publicacion_detalle, name='publicacion_detalle'),
    url(r'^post/nueva/$', views.publicacion_nueva, name='publicacion_nueva'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.publicacion_editar, name='publicacion_editar'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]
