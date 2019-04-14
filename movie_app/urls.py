from django.urls import path
from movie_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.movie_details, name='movie_details')
]
