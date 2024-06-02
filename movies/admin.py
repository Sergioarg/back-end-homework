from django.contrib import admin
from movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    """ Register Movie model """
    list_filter = ('user', 'year', 'original_lang')
    list_display = ('id', 'title', 'year', 'is_private', 'genre', 'director', 'cast')
    search_fields = ('user', 'title', 'year', 'original_lang')

admin.site.register(Movie, MovieAdmin)
