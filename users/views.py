from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import User
# Create your views here.
class UserFilterView(ListView):
    template_name = 'users/index.html'
    model = User

    queryset = User.objects.all()
