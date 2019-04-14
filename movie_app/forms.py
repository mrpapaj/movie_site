from django import forms


class FormMovie(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder': 'Movie title'}), label='')
