from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Home")
    return render(request, "homepage.html")

def about(request):
    #return HttpResponse("This project is in progress. It will be a music based social media site")
    return render(request, "about.html")
