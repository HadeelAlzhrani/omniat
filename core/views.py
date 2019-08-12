from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.

def home_view(request):
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request):
    return render(request, "contact.html", {})

def about_view(request):
    #my_context = {
    #   "title": "this is about us",
    #    "this_is_true": True,
    #    "my_number": 123,
    #    "my_list": [1313,4231,312, "Abc"],
    #    "my_html": "<h1> Hello World </h1>"
    #}
    return render(request, "about.html", {})

def social_view(request):
    return HttpResponse ("<h1> Social Page</h1>")

def wish_create_view(request):
    form = WishForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "wish_create.html", context)


def comment_create_view(request):
    form = CommentForm (request.POST or None)
    if form.is_valid():
        form.save()


    context = {
        'form': form
    }
    return render(request, "comment_create.html", context)

