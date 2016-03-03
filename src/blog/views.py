from django.shortcuts import render

# Create your views here.

from .forms import TestForm

def home(request):
    form = TestForm()
    return render(request, "forms.html", {"form": form})