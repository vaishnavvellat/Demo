from django import forms
from .models import Movie


class MovieForms(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'image']
