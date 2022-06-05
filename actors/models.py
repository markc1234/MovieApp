from django.db import models


# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nacionality = models.ForeignKey('Nacionality', on_delete=models.CASCADE)
    born_date = models.DateField()
    picture = models.ImageField(blank=True)
    biographical_summary = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Nacionality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name