from django.shortcuts import render

# Create your views here.

from .forms import TestForm

def home(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        print(form.cleaned_data.get("some_text"))
        print(form.cleaned_data.get("email"))
        print(form.cleaned_data.get("email2"))

    # if request.method == "POST":
    #     form = TestForm(request.POST)
    #     print(request.POST)
    #     print(request.POST.get("username")) #None
    #     #print(request.POST["username2"]) #Raise error
    # elif request.method == "GET":
    #     form = TestForm()
    #     print(request.GET)
    return render(request, "forms.html", {"form": form})