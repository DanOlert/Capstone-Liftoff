from django.shortcuts import render, redirect
from django.http import HttpResponse

#TODO learn more about decorators in python
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/user/login/")
def api_list(request):
    return render(request, 'apis/api_list.html') #TODO pass in list of apis and teir login status

@login_required(login_url="/user/login/")
def spotify(request):
    return render(request, 'apis/spotify.html')
