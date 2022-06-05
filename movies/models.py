from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from actors.models import Actor
from directors.models import Director


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class MovieManager(models.Manager):
    def getBest12():
        pass


class Movie(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    actors = models.ManyToManyField(Actor, blank=True)
    year_of_production = models.DateField()
    picture = models.ImageField(blank=True)
    film_director = models.ForeignKey(Director, on_delete=models.RESTRICT, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    objects =  MovieManager()


    def getRatingAverage(self):
        all_ratings = self.Review.all()
        count = 0

        for rating in all_ratings:
            total += rating.rating
            count += 1

        return total // count

    def __str__(self):
        return self.title

        
class Review(models.Model):
    email = models.EmailField(max_length=200, blank=True)
    username=models.CharField(max_length=60, blank=True)
    source = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    approved = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)