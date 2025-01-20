from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'bio', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categorias']
        widgets = {
            'categorias': forms.CheckboxSelectMultiple(),  # Cambia el widget para categorías
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Search Posts', max_length=100)