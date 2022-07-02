import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


# Create your models here.
class Actor(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nacionality = models.ForeignKey('Nacionality', on_delete=models.CASCADE)
    born_date = models.DateField()
    picture = models.ImageField(blank=True, upload_to='actors/')
    biographical_summary = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("actor_detail", args=[str(self.id)])


class Director(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nacionality = models.ForeignKey('Nacionality', on_delete=models.CASCADE)
    born_date = models.DateField()
    picture = models.ImageField(blank=True, upload_to='directors/')
    biographical_summary = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("director_detail", args=[str(self.id)])


class Nacionality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MovieManager(models.Manager):
    def getBest12():
        pass


class Movie(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    actors = models.ManyToManyField(Actor, blank=True)
    year_of_production = models.DateField()
    picture = models.ImageField(blank=True, upload_to='movies/')
    film_director = models.ForeignKey(Director, on_delete=models.RESTRICT, blank=True)
    objects =  MovieManager()

    def getRatingAverage(self):
        all_ratings = Review.all()
        count = 0

        for rating in all_ratings:
            total += rating.rating
            count += 1

        return total // count

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.id)])

        
class Review(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default=uuid.uuid4,
        editable=False
    )
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

    def __str__(self):
        return self.source
