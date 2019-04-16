from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .forms import FormFavorite
import requests


def movie_details(request):
    form = forms.FormMovie()
    if request.method == 'POST':

        if 'btnSearch' in request.POST:
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
                            'insert_response': 'True',
                    }
                    return render(request, 'movie_app/search_movies.html', context=movie_info)

        elif 'btnAdd' in request.POST:
            form = FormFavorite(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'movie_app/search_movies.html', context={'form': form})

    return render(request, 'movie_app/search_movies.html', context={'form': form, 'insert_response': 'False'})


def fav_movies(request):
    my_movies = {'insert_favorites': 'Your favorite movies.'}
    return render(request, 'movie_app/favorite_movies.html', context=my_movies)
