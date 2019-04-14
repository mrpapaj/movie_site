from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_msg': "This is your home page"}
    return render(request, 'movie_app/index.html', context=my_dict)
