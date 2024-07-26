from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class PublicationsView(TemplateView):
    template_name = 'publication-detail.html'

class AboutView(TemplateView):
    template_name = 'about.html'
