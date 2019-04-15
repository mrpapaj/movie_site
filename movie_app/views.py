from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import requests
# Create your views here.

def index(request):
    my_dict = {'insert_msg': 'This is your home page'}
    return render(request, 'movie_app/index.html', context=my_dict)

def movie_details(request):
    form = forms.FormMovie()
    default_dict = {
            'form': form,
            'insert_poster': '/static/search_icon.png'
    }
    if request.method == 'POST':
        form = forms.FormMovie(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['title']
            response = requests.get('http://www.omdbapi.com/?t=' + user_input, params={'apikey': 'adedb5e4'})
            data = response.json()
            if data['Response'] == 'True':
                movie_info = {
                        'form': form,
                        'insert_title': 'Title: ' + data['Title'],
                        'insert_director': 'Director: ' + data['Director'],
                        'insert_genre': 'Genre: ' + data['Genre'],
                        'insert_plot': 'Plot: ' + data['Plot'],
                        'insert_poster': data['Poster'],
                        'insert_runtime': 'Time: ' + data['Runtime'],
                        'insert_release': 'Release date: ' + data['Released'],
                }
                return render(request, 'movie_app/base.html', context=movie_info)
    return render(request, 'movie_app/base.html', context=default_dict)
