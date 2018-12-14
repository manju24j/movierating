from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Rater(models.Model):
    user = models.OneToOneField(User)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.username

class Movie(models.Model):
    name = models.CharField(max_length=64)
    tagline = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    year = models.IntegerField(default=2014,max_length=64)
    image = models.URLField()
    live = models.BooleanField(default=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    rating_count = models.IntegerField(default=0, blank=True)
    rating_sum = models.IntegerField(default=0, blank=True)

    def _get_average_rating(self):
        if self.rating_count == 0:
            return 0.0
        else:
            return round(float(self.rating_sum)/float(self.rating_count),1)

    rating_average = property(_get_average_rating)

    def __unicode__(self):
        return self.name


RATING_CHOICES = ( (1,'1'),(2,'2'),
    (3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),
    (8,'8'),(9,'9'),(10,'10')
)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    comment = models.CharField(max_length=512)
    score = models.IntegerField(default=1, choices=RATING_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.score) + ' ' + self.comment


class Bookmark(models.Model):
    user = models.ForeignKey(User,default=1)
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    date = models.DateTimeField(auto_now_add=True)
