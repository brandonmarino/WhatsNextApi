"""whatsnextapiadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from whatsnextapi import views as whatsnextapi_views
from login import views as login_views
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'users', whatsnextapi_views.UserViewSet)
router.register(r'groups', whatsnextapi_views.GroupViewSet)
router.register(r'productions', whatsnextapi_views.ProductionViewSet)
router.register(r'movies', whatsnextapi_views.MovieViewSet)
router.register(r'shows', whatsnextapi_views.ShowViewSet)
router.register(r'seasons', whatsnextapi_views.SeasonViewSet)
router.register(r'watchlists', whatsnextapi_views.WatchListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/rest/', include('rest_auth.urls')),
    path('auth/login/',  login_views.LoginViewPage.as_view(), name='rest_login'),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', get_schema_view()),
    path('api/', include(router.urls)),
]
