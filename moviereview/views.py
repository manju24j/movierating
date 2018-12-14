from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import viewsets,status

from models import Movie, Category,Rating, Rater
from moviereview.serializers import UserSerializer,MovieSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


def signin(request):
    if request.user.is_authenticated():
	    data="user already logged in"
	    return HttpResponse(json.dumps(data),content_type="application/json")

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponse(json.dumps("success"),content_type="application/json")
        else:
            # Show an error page
            return HttpResponse(json.dumps("username or password wrong"),content_type="application/json")
    else:
        return HttpResponse(json.dumps("username or password wrong"),content_type="application/json")

def get_rater(user):
    if user.is_anonymous():
        return None
    r = Rater.objects.filter(user=user)
    if len(r) == 1:
        return r[0]
    else:
        return None

@login_required
def movie_rate(request, movieid):
    context = RequestContext(request)
    context_dict ={}
    rater = get_rater(request.user)
    if rater:
        if request.method == 'POST':
            movie = Movie.objects.get(id=movieid)
            # check if the rater has already rated this app, if so, remove this entry and replace with new rating
            rating_check = Rating.objects.filter(rater=rater,movie=movie).count()
            if rating_check == 1:
                past_rating = Rating.objects.get(rater=rater,movie=movie)
                movie.rating_count = movie.rating_count - 1
                movie.rating_sum = movie.rating_sum - past_rating.score
                past_rating.delete()
                movie.save()

            rating = rating_form.save(commit=False)
            rating.rater = rater
            rating.movie = movie
            rating.save()
            movie.rating_count = movie.rating_count + 1
            movie.rating_sum = movie.rating_sum + rating.score
            movie.save()
            return HttpResponse(json.dumps("success"),content_type="application/json")
        else:
		    return HttpResponse(json.dumps("error"),content_type="application/json")

