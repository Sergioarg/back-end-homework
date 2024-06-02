from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    """ Represetantional model Movie """

    title = models.CharField(max_length=100)
    description = models.TextField()
    # genre = models.ManyToManyField(Genre, blank=True)
    year = models.IntegerField()
    cast = models.CharField(max_length=200)
    director = models.CharField(max_length=100, blank=True, null=True) #opt
    created_at = models.DateTimeField(auto_now_add=True)
    original_lang = models.CharField(
        max_length=10,
        help_text='Enter a original language (e.g. en)'
    )
    update_at = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=True)
    duration = models.FloatField(
        max_length=3, help_text='Enter a duration in hours (e.g. 1.50)'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
