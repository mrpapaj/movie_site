from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    my_dict = {'insert_msg': "This is your home page"}
    return render(request, 'movie_app/index.html', context=my_dict)

def movie_details(request):
    movie_title = "Dragon"
    response = requests.get("http://www.omdbapi.com/?t=" + movie_title, params={'apikey': "adedb5e4"})
    data = response.text
    movie_info = {'insert_movie': data}
    return render(request, 'movie_app/search_movies.html', context=movie_info)
