
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Cheese

class CheeseListView(ListView):
    model=Cheese
    template_name="cheeses/cheeses.html"
    context_object_name="cheeses"

# Create your views here.
