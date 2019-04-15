from django.urls import path
from movie_app import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login_page'),
    path('index/', views.index, name='index'),
    path('movie/', views.movie_details, name='search_movies'),
]
