from django.conf.urls import patterns, url
from moviereview import views
from . import api_views

urlpatterns = patterns('',

        url(r'^api/addmovie/$', api_views.AddMovie.as_view()),
        url(r'^api/moviedetails/(?P<pk>[0-9]+)/$', api_views.EditMoive.as_view()),

        url(r'^ratemovie/(?P<movieid>[0-9]+)/$', views.movie_rate, name='movie_rate'),
        url(r'^api/addrating/$', api_views.AddRating.as_view()),
        url(r'^api/ratingdetails/(?P<pk>[0-9]+)/$', api_views.EditRating.as_view()),
        url(r'^api/deleterating/(?P<pk>[0-9]+)/$', api_views.DeleteRating.as_view()),

)
