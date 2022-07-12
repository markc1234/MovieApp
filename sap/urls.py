from django.urls import path
from .views import (HomePageView, ActorListView, ActorDetailView, MovieListView, MovieDetailView,
                    DirectorListView, DirectorDetailView, MovieCreateView,
                    SearchMoviesResultsListView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('actors/', ActorListView.as_view(), name='actor_list'),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('directors/', DirectorListView.as_view(), name='director_list'),
    path('actor/<uuid:pk>/', ActorDetailView.as_view(), name='actor_detail'),
    path('movie/<uuid:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('director/<uuid:pk>/', DirectorDetailView.as_view(), name='director_detail'),
    path('movie/new/', MovieCreateView.as_view(), name='movie_new'),
    path('movie/search/', SearchMoviesResultsListView.as_view(), name='search_movie_results'),
]