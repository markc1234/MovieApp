from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from actors.models import Actor
from directors.models import Director


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Review(models.Model):
    source = models.TextField(max_length=500)
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )


class Movie(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    actors = models.ManyToManyField(Actor, blank=True)
    year_of_production = models.DateField()
    film_director = models.ForeignKey(Director, on_delete=models.CASCADE)
    reviews = models.ManyToManyField(Review, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
