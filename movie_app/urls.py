from django.urls import path
from movie_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie_details, name='movie_details')
]
