from django import forms
from .models import MovieGenre, Movie, Review, Tickets


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'movie_genre', 'description', 'released_date')


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = MovieGenre
        fields = ('id', 'name')


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'rating', 'review', 'date')


class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'movie_genre', 'description', 'released_date')


class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('user', 'address', 'contact', 'number_of_tickets')
