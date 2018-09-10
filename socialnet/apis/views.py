from django.shortcuts import render, redirect
from django.http import HttpResponse
# NOTE Commenting out spotify crap for now
# from .spotipy_user_auth import getSpotifyToken
#spotify and json stuff
# import os
# import sys
# import json
# import spotipy
# import spotipy.util as util
# from json.decoder import JSONDecodeError


#TODO learn more about decorators in python
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/user/login/")
def api_list(request):
    return render(request, 'apis/api_list.html') #TODO pass in list of apis and their login status

@login_required(login_url="/user/login/")
def spotify(request):
    #TODO refresh login info from database, rather than hardcoded 'username'
    username = '1246393108'
    #TODO expand scope as needed for features
    scope = "user-library-read"
    if request.method == 'POST':
        #NOTE commenting out spotify crap for now
        # token = getSpotifyToken(username, scope)
        # #TODO if token check!
        # spotifyObject = spotipy.Spotify(auth=token)
        # spotifyUser = spotifyObject.current_user()
        # print(token)
        # print(spotifyUser['display_name'])
        return redirect('apis:list')
    else:
        return render(request, 'apis/spotify.html')

@login_required(login_url="/user/login/")
def soundcloud(request):
    return render(request, 'apis/soundcloud.html')
