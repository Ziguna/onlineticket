from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MovieGenre, Movie, Review
from django.core.urlresolvers import reverse_lazy
from polls.forms import MovieCreateForm, GenreCreateForm, ReviewCreateForm, MovieUpdateForm, TicketBookingForm


class GenreListView(ListView):
    '''
    Used to show the list of all the genres in the main page.
    '''
    model = MovieGenre
    template_name = "genrelist.html"

    def get_context_data(self, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        return context


class GenreDetailView(DetailView):
    '''
    Used to show the list of all the movies inside a particular genre
    '''
    model = MovieGenre
    template_name = "movie.html"

    def get_context_data(self, **kwargs):
        context = super(GenreDetailView, self).get_context_data(**kwargs)
        context['a'] = Movie.objects.all()
        return context


class CreateMovieGenre(CreateView):
    '''
    Used to create a new movie genre
    '''
    template_name = "CreateMovieGenre.html"
    form_class = GenreCreateForm

    success_url = reverse_lazy('MovieListView')


class MovieDetailView(DetailView):
    '''
    Used to show all the details about a particular movie
    '''

    model = Movie
    template_name = "moviedetail.html"

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        return context


class MovieCreateView(CreateView):
    '''
    Used to create a new movie in a particular genre
    '''
    template_name = "showmovie.html"
    form_class = MovieCreateForm

    success_url = reverse_lazy('MovieListView')

    def get_initial(self):
        initials = super(MovieCreateView, self).get_initial()
        initials['movie_genre'] = self.kwargs['pk']

        return initials


class ReviewCreateView(CreateView):
    '''
    Used to ADD the reviews and ratings of a particular movie
    '''
    template_name = "addreview.html"
    form_class = ReviewCreateForm

    success_url = reverse_lazy('MovieListView')


class ReviewDetailView(DetailView):
    '''
    Used to SHOW all the reviews and ratings of the particular movie
    '''
    model = Review
    template_name = "moviedetail.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewDetailView, self).get_context_data(**kwargs)
        return context


class MovieUpdateView(UpdateView):
    '''
    Used to update the name, description, relesed date of the particular movie in this section
    '''
    model = Movie
    template_name = "updatemovie.html"
    form_class = MovieUpdateForm

    success_url = reverse_lazy('MovieListView')


class MovieDeleteView(DeleteView):
    '''
    Used to delete the movie and return it to the main page.
    '''
    model = Movie
    template_name = "deletemovie.html"
    field = [
    ]
    success_url = reverse_lazy('MovieListView')


class GenreDeleteView(DeleteView):
    '''
    Used to delete the particular genre and return it to the main page.
    '''
    model = MovieGenre
    template_name = "deletegenre.html"
    field = [
    ]
    success_url = reverse_lazy('MovieListView')


class TicketBookingView(CreateView):
    '''
    Used to add the name, address and number of tickets the user booked for the movie.
    '''
    template_name = "booking.html"
    form_class = TicketBookingForm
    success_url = reverse_lazy('MovieListView')
