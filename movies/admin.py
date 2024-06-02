from django.contrib import admin
from movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    """ Register Movie model """
    list_filter = ('user', 'year')
    list_display = ('id', 'title', 'year', 'private', 'director', 'cast')
    search_fields = ('user', 'title', 'year', 'original_lang')

admin.site.register(Movie, MovieAdmin)
