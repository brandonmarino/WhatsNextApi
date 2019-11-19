from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from whatsnextapi.serializers import UserSerializer, GroupSerializer, ProductionSerializer, MovieSerializer, ShowSerializer, SeasonSerializer, WatchListSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProductionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows productions to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = ProductionSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = MovieSerializer

class ShowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shows to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = ShowSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows seasons to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = SeasonSerializer

class WatchListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows watchlists to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = WatchListSerializer
