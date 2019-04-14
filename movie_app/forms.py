from django import forms


class FormMovie(forms.Form):
    title = forms.CharField()
