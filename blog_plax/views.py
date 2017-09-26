from django.shortcuts import render
from .models import *

def post_list(request):
    publicaciones= Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'publicaciones':publicaciones})
