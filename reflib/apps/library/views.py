from django.shortcuts import render
from django.views.generic import TemplateView


class LibraryBaseView (TemplateView):
    template_name = 'library/home.html'
