from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm, SearchForm
from .models import Autor, Categoria, Post

# Create your views here.

def index(request):
    return render(request, 'AppBlog/index.html')

def nuevo_autor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
    else:
        autor_form = AutorForm()
    return render(request, 'AppBlog/nuevo_autor.html', {'autor_form': autor_form})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'AppBlog/lista_autores.html', {'autores': autores})

def nuevo_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
    else:
        post_form = PostForm()
    return render(request, 'AppBlog/nuevo_post.html', {'post_form': post_form})

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'AppBlog/lista_posts.html', {'posts': posts})

def nuevo_categoria(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
    else:
        categoria_form = CategoriaForm()
    return render(request, 'AppBlog/nuevo_categoria.html', {'categoria_form': categoria_form})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'AppBlog/lista_categorias.html', {'categorias': categorias})


def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            posts = Post.objects.filter(titulo__icontains=query)
            return render(request, 'AppBlog/search.html', {'posts': posts, 'query': query})
    else:
        search_form = SearchForm()
    return render(request, 'AppBlog/search.html', {'search_form': search_form})