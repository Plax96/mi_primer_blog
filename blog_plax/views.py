from django.shortcuts import render, get_object_or_404
from .models import *

def post_list(request):
    publicaciones= Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'publicaciones':publicaciones})

def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, id=pk)
    return render(request, 'blog/publicacion_detalle.html', {'publicacion': publicacion})
