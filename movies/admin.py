""" Register models of Movie app """
from django.contrib import admin
from movies.models import Movie, Genre

class GenreAdmin(admin.ModelAdmin):
    """ Register Genre model """
    list_display = ('name',)

class MovieAdmin(admin.ModelAdmin):
    """ Register Movie model """
    list_filter = ('user', 'year')
    list_display = ('title', 'year', 'private', 'director', 'cast')
    search_fields = ('user', 'title', 'year', 'original_lang')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
