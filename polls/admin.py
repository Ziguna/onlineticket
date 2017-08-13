from django.contrib import admin
from polls.models import *
from polls.models import MovieGenre, Movie, Tickets, Review



# Register your models here.
admin.site.register(MovieGenre)
admin.site.register(Movie)
admin.site.register(Tickets)
admin.site.register(Review)


