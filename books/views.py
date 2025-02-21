from django.shortcuts import render                         # imported by default
from django.views.generic import ListView, DetailView       # to display lists
from .models import Book                                    # to access Book model
from django.contrib.auth.mixins import LoginRequiredMixin   # to protect class-based view

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):           # class-based "protected" view
  model = Book                                              # specify model
  template_name = 'books/main.html'                         # specify template

class BookDetailView(LoginRequiredMixin, DetailView):       # class-based "protected" view
  model = Book                                              # specify model
  template_name = 'books/detail.html'                       # specify template