from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers, viewsets, routers

from moviereview.models import User, Movie, Category,Rating, Rater
from .serializers import UserSerializer,MovieSerializer,RatingSerializer

#---------- Movie MODEL --------------------

class AddMovie(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class EditMoive(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class DeleteMovie(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

#---------- Rating MODEL --------------------

class AddRating(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class EditRating(generics.RetrieveUpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class DeleteRating(generics.RetrieveDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
