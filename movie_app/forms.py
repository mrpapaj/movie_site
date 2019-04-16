from django import forms
from movie_app.models import Favorite


class FormMovie(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder': 'Movie title'}), label='')


class FormFavorite(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ['title', 'user']
