from django.urls import path
from .views import index, nuevo_autor, lista_autores, nuevo_post, lista_posts, lista_categorias, nuevo_categoria, search

urlpatterns = [
    path('', index, name='index'),
    path('nuevo_autor/', nuevo_autor, name='nuevo_autor'),
    path('lista_autores/', lista_autores, name='lista_autores'),
    path('nuevo_post/', nuevo_post, name='nuevo_post'),
    path('lista_posts/', lista_posts, name='lista_posts'),
    path('nuevo_categoria/', nuevo_categoria, name='nuevo_categoria'),
    path('lista_categorias/', lista_categorias, name='lista_categorias'),
    path('search/', search, name='search'),
]
