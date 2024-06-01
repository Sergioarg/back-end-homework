from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a movie genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name

class Movie(models.Model):

    adult = models.BooleanField(default=False)

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, blank=True)

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
        validators=[MinValueValidator(0.0), MaxLengthValidator(9.00)],
        help_text='Enter a duration in hours (e.g. 1.5)'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
