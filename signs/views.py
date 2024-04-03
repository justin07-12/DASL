from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class SignFilterView(TemplateView):
    template_name = 'signs/index.html'
