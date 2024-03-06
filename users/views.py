from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class UserFilterView(TemplateView):
    template_name = 'users/index.html'
