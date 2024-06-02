from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    """ Represetantional model Movie """
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True)
    year = models.IntegerField()
    cast = models.CharField(max_length=200)

    original_lang = models.CharField(
        max_length=10,
        help_text='Enter a original language (e.g. en)'
    )
    is_private = models.BooleanField(default=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
