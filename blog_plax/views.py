from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PublicacionForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    publicaciones= Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'publicaciones':publicaciones})

@login_required
def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, id=pk)
    return render(request, 'blog/publicacion_detalle.html', {'publicacion': publicacion})

@login_required
def publicacion_nueva(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('publicacion_detalle', pk=post.pk)
    else:
        form = PublicacionForm()
    return render(request, 'blog/publicacion_editar.html', {'form': form})

@login_required
def publicacion_editar(request, pk):
    post = get_object_or_404(Publicacion, id=pk)
    if request.method == "POST":
        form = PublicacionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('publicacion_detalle', pk=post.pk)
    else:
        form = PublicacionForm(instance=post)
    return render(request, 'blog/publicacion_editar.html', {'form': form})

@login_required
def publicacion_publicar(request, pk):
    post = get_object_or_404(Publicacion, id=pk)
    post.publish()
    return redirect('publicacion_detalle', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()

@login_required
def publicacion_lista_borrador(request):
    pub = Publicacion.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/borrador.html', {'posts': pub})

@login_required
def publicar_remover(request, pk):
    post = get_object_or_404(Publicacion, id=pk)
    post.delete()
    return redirect('post_list')
