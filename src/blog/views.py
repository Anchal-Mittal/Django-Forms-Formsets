from django.shortcuts import render

# Create your views here.

from .forms import SearchForm

def home(request):
    form = SearchForm()
    return render(request, "forms.html", {"form": form})