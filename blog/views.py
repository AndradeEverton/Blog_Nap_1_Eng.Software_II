from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from .forms import ComentarioForm
from django.contrib import messages
from django.utils.timezone import now


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def detalhes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comentarios = Comentario.objects.filter(post=post)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            messages.success(request, '✔ Comentário adicionado com sucesso!')
            return redirect('index')
    else:
        form = ComentarioForm()

    return render(request, 'blog/detalhes.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })