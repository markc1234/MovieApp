from django.contrib import admin
from .models import Actor, Nacionality, Director, Movie, Review

# Register your models here.
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'nacionality', 'born_date',)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'nacionality', 'born_date',)


class ReviewInline(admin.TabularInline):
    model = Review


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ('title', 'film_director', 'year_of_production', 'summary', 'film_director', 'get_actors')

    def get_actors(self, obj):
        return " - ".join([actor.first_name for actor in obj.actors.all()])


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('username', 'source',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)


admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Nacionality)