from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>\d+)/$', views.publicacion_detalle, name='publicacion_detalle'),
]
