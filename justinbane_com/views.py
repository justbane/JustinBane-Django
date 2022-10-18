from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "name": "Justin Bane",
        "greeting": "Hello there!!"
    }
    return render(request, "index.html", context)