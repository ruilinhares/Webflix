
from django.urls import path, include

from . import views


urlpatterns = [
    path('home/', views.suggested_movies, name='homepage'),
    path('register/', views.signup, name='register'),

    path('profile/', views.view_profile, name='profile'),
    path('profile/edit', views.edit_profile, name='editprofile'),
    path('movie/mymovies', views.view_list_movies, name='movielist'),
    path('movie/searchbar', views.search_bar, name='searchbar'),
    path('movie/search', views.search_movies, name='searchmovie'),
    path('movie/delete_movie/<int:id>', views.delete_movie, name='deletemovie'),
    path('movie/add_movie/<int:id>', views.add_movie, name='addmovie'),
]
