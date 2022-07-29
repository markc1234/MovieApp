from http.client import HTTPResponse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, View
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy

from .models import Movie, Actor, Director, Review

# Create your views here.
class HomePageView(ListView):
    model = Movie
    context_object_name = 'best12movies'
    template_name = 'home.html'


# MOVIES
class MovieListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    movie = Movie()

    def get_context_data(self, **kwargs):
        pk_movie = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['movie'] = Movie.objects.get(pk=pk_movie)
        self.movie = Movie.objects.get(pk=pk_movie)
        context['director'] = Director.objects.filter(movie=self.movie)
        context['actors'] = Actor.objects.filter(movie=self.movie)
        context['reviews'] = Review.objects.filter(movie=self.movie)
        return context


class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Movie
    template_name = 'movies/movie_new.html'
    fields = ('title', 'summary', 'actors', 'year_of_production', 'picture', 'film_director')
    success_url = reverse_lazy('movie_list')
    login_url = 'account_login'
    permission_required = 'movies.create_movie'


# REVIEWS
class ReviewAdminCheckingView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Review
    context_object_name = 'review_list'
    template_name = 'reviews/admin_check.html'
    login_url = 'account_login'
    permission_required = 'movies.see_new_reviews'


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'reviews/review_new.html'
    fields = ('email', 'username', 'source', 'rating', 'movie')
    
    def get_success_url(self) -> str:
        movie_id = self.object.movie.id
        return reverse_lazy('movie_detail',  args=[str(movie_id)])

class ReviewApprovedUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'reviews/review_update_approve.html'
    fields = ('approved', )
    success_url = reverse_lazy('admin_check')
    login_url = 'account_login'
    permission_required = 'movies.approve_review'


class ReviewDisapprovedUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'reviews/review_update_disapprove.html'
    fields = ('disapproved', )
    success_url = reverse_lazy('admin_check')
    login_url = 'account_login'
    permission_required = 'movies.disapprove_review'


# ACTORS
class ActorListView(ListView):
    model = Actor
    context_object_name = 'actor_list'
    template_name ='actors/actor_list.html'


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'actors/actor_detail.html'
    actor = Actor()

    def get_context_data(self, **kwargs):
        pk_actor = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['actor'] = Actor.objects.get(pk = pk_actor)
        self.actor = Actor.objects.get(pk=pk_actor)
        context['movies'] = Movie.objects.filter(actors = self.actor)
        return context


# DIRECTORS
class DirectorListView(ListView):
    model = Director
    context_object_name = 'director_list'
    template_name = 'directors/director_list.html'


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'directors/director_detail.html'
    director = Director()
    
    def get_context_data(self, **kwargs):
        pk_director = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['director'] = Director.objects.get(pk = pk_director)
        self.director = Director.objects.get(pk=pk_director)
        context['movies'] = Movie.objects.filter(film_director = self.director)
        return context


# SEARCH

class SearchMoviesResultsListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/search_movie_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Movie.objects.filter(
            Q(title__icontains=query) |
            Q(year_of_production__icontains=query) |
            Q(film_director__last_name__icontains=query) |
            Q(film_director__first_name__icontains=query) |
            Q(actors__last_name__icontains=query) |
            Q(actors__first_name__icontains=query)  
        ).distinct()


class SearchActorsResultsListView(ListView):
    model = Actor
    context_object_name = 'actor_list'
    template_name = 'actors/search_actor_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Actor.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(born_date__icontains=query) |
            Q(nacionality__name__icontains=query)
        ).distinct()


class SearchDirectorsResultsListView(ListView):
    model = Director
    context_object_name = 'director_list'
    template_name = 'directors/search_director_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Director.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(born_date__icontains=query) |
            Q(nacionality__name__icontains=query)
        ).distinct()