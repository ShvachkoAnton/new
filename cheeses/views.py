
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Cheese
from django.contrib.auth.mixins import LoginRequiredMixin


class CheeseListView(ListView):
    model = Cheese
    template_name = "cheeses/cheeses.html"
    context_object_name = "cheeses"


class CheeseDetailView(DetailView):
    model = Cheese
    template_name = "cheeses/cheese_detail.html"
# Create your views here.


class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    template_name = "cheeses/create.html"
    fields = ['name', 'description', 'firmness', 'country_of_origin']
    def form_valid(self,form):
        form.instance.creator=self.request.user
        return super().form_valid(form)
    