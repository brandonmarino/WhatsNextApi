from django.shortcuts import render
from django.views.generic import TemplateView

class LoginViewPage(TemplateView):
    template_name = 'login.html'
