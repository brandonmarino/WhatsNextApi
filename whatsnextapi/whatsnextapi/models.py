from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

class Production(PolymorphicModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Movie(Production):
    tmdb_url = models.CharField(max_length=100)
    watched = models.BooleanField()

class Show(Production):
    tvdb_url = models.CharField(max_length=100)
    watched = models.SmallIntegerField()

class Season(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    season = models.SmallIntegerField()
    episodes = models.SmallIntegerField()
    
    def __str__(self):
        return f'Season {season} - Episodes Watched {episodes}'

class WatchList(models.Model):
    name = models.CharField(max_length=100)
    productions = models.ManyToManyField(Production)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

