from django.contrib.auth.models import User, Group
from rest_framework import serializers
from whatsnextapi.models import Production, Movie, Show, Season, WatchList

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ['title']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'tmdb_url', 'watched']

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ['title', 'tvdb_url', 'watched']

class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        show = ShowSerializer(many=False, required=True)
        fields = ['season', 'episodes', 'show']

class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WatchList
        fields = ['name', 'productions', 'members']
        productions = ProductionSerializer(many=True, required=True)
        members = UserSerializer(many=True, required=True)
