from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Movie, Actor, Director

# Create your views here.
class HomePageView(ListView):
    model = Movie
    context_object_name = 'best12movies'
    template_name = 'home.html'


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/movie_detail.html'


class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Movie
    template_name = 'movies/movie_new.html'
    fields = ('title', 'summary', 'actors', 'year_of_production', 'picture', 'film_director')
    login_url = 'account_login'
    permission_required = 'movies.create_movie'


class ActorListView(ListView):
    model = Actor
    context_object_name = 'actor_list'
    template_name ='actors/actor_list.html'


class ActorDetailView(DetailView):
    model = Actor
    context_object_name = 'actor'
    template_name = 'actors/actor_detail.html'


class DirectorListView(ListView):
    model = Director
    context_object_name = 'director_list'
    template_name = 'directors/director_list.html'


class DirectorDetailView(DetailView):
    model = Director
    context_object_name = 'director'
    template_name = 'directors/director_detail.html'

# SEARCH

class SearchMoviesResultsListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/search_movie_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Movie.objects.filter(
            Q(title__icontains=query)
        )
