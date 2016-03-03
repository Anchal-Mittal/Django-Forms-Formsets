from django.shortcuts import render

# Create your views here.

from .forms import TestForm

def home(request):
    form = TestForm()
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("username")) #None
        #print(request.POST["username2"]) #Raise error
    elif request.method == "GET":
        print(request.GET)
    return render(request, "forms.html", {"form": form})