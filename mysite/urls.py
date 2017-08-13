"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.conf.urls import url
from polls import views as v

app_name = "polls"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', v.GenreListView.as_view(), name="MovieListView"),
    url(r'^CreateMovieGenre/$', v.CreateMovieGenre.as_view(), name="CreateMovieGenre"),
    url(r'^showmovies/(?P<pk>\d+)/$', v.MovieCreateView.as_view(), name="CreateNewMovie"),
    url(r'^(?P<pk>\d+)/$', v.MovieDetailView.as_view(), name="MovieDetailView"),
    url(r'^showmovie/(?P<pk>\d+)/$', v.GenreDetailView.as_view(), name="genreshow"),
    url(r'^moviedetail/(?P<pk>\d+)/$', v.MovieDetailView.as_view(), name="moviedetail"),
    url(r'^updatemoviedetail/(?P<pk>\d+)/$', v.MovieUpdateView.as_view(), name="updatemovie"),
    url(r'^deletemoviedetail/(?P<pk>\d+)/$', v.MovieDeleteView.as_view(), name="deletemovie"),
    url(r'^deletegenre/(?P<pk>\d+)/$', v.GenreDeleteView.as_view(), name="deletegenre"),
    url(r'^addreview/(?P<pk>\d+)/$', v.ReviewCreateView.as_view(), name="addreview"),
    url(r'^showreview/(?P<pk>\d+)/$', v.ReviewDetailView.as_view(), name="showreview"),
    url(r'^ticketbooking/(?P<pk>\d+)/$', v.TicketBookingView.as_view(), name="bookticket")

]
