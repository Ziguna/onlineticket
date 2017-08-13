from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date


class MovieGenre(models.Model):
    '''
    Used to store all the names of the movie genres.
    '''

    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    '''
    Used to store the name, genre, plot and released date of the movies.
    '''

    name = models.CharField(blank=True, max_length=100)
    movie_genre = models.ForeignKey(MovieGenre, blank=True)
    description = models.TextField(blank=True)
    released_date = models.DateField(default=date.today)

    def __str__(self):
        return self.name + str(self.movie_genre) + self.description


class Tickets(models.Model):
    '''
    Used to store the description of users who book the tickets for the particular movie.
    '''

    user = models.OneToOneField(User, blank=True)
    address = models.CharField(blank=True, max_length=100)
    contact = models.IntegerField(blank=True, validators=[MaxValueValidator(10), MinValueValidator(10)])
    number_of_tickets = models.IntegerField(blank=True, default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return str(self.user) + self.address + str(self.contact) + str(self.number_of_tickets)


class Review(models.Model):
    '''
    Used to store all the ratings and review given to the movie by the particular user.
    '''
    name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField('Rating(stars)', blank=True, default=2, validators=[MaxValueValidator(5)])
    review = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.name) + str(self.rating) + self.review + str(self.date)
