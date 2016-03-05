from django.shortcuts import render
from django.utils import timezone
# Create your views here.

from .forms import TestForm, PostModelForm

def home(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj.title)
        obj.title = "Some random title"
        obj.publish = timezone.now()
        obj.save()
    # initial_dict = {
    #     #"some_text": "Text",
    #     "boolean": True,
    #     # "integer": "123"
    # }
    # form = TestForm(request.POST or None, initial=initial_dict)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     print(form.cleaned_data.get("some_text"))
    #     print(form.cleaned_data.get("email"))
    #     print(form.cleaned_data.get("email2"))

    # if request.method == "POST":
    #     form = TestForm(data=request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         print(form.cleaned_data.get("some_text"))
    #     #print(request.POST)
    #     #print(request.POST.get("username")) #None
    #     #print(request.POST["username2"]) #Raise error
    # elif request.method == "GET":
    #     form = TestForm(user=request.user)
    #     print(request.GET)

    return render(request, "forms.html", {"form": form})