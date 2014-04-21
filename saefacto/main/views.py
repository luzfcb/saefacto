from braces.views import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import generic


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/home.html'
