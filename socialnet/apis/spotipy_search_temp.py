import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError



# User ID: 1246393108?si=rfxxo5j8RT2pDGD_TJEbaA (is the get request included? I dont think so)
# Client ID: 284e9c8ac07046ac9e1443a4ab3bb4df (check spotify if changed)

# Erase cache and prompt user permisions


scope = 'user-library-read'

#NOTE Use this if User ID is not supplied
# username = sys.argv[1]
#
# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print ("Please enter username as second arguement.")
#     sys.exit()

username = '1246393108'

try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cashe-{username}")
    token = util.prompt_for_user_token(username, scope)


#spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']
spotifyLink = user['external_urls']['spotify']

#TODO console practice. need to change to work in web browser
while True:

    print()
    print('>>> Welcome ' + displayName)
    print('Open App '+ spotifyLink)
    print('0 to exit')
    print('1 to search')
    choice = input('your choice: ')

    if choice == '1':
        print()
        searchQuery = input ("Search Term: ")
        print()

        searchResultsArtist = spotifyObject.search(searchQuery,4,0,'artist')['artists']['items']
        searchResultsTrack = spotifyObject.search(searchQuery,6,0,'track')['tracks']['items']
        searchResultsAlbum = spotifyObject.search(searchQuery,4,0,'album')['albums']['items']

        #this for loop can go in a template maybe with some javascript

        if searchResultsArtist:
            for artist in searchResultsArtist:
                print()
                print(artist['name'])
                print(artist['href'])
                print(artist['uri'])
                print(artist['id'])
                print("Image: " + artist['images'][0]['url'])
                print()
        else:
            print()
            print("No Artist Results")
            print()

            #NOTE view all albums in artist from console:
            #artist_albums = spotifyObject.artist_albums(artistID)
            #print(json.dumps(artist_albums, sort_keys=True, indent=4))
        if searchResultsAlbum:
            for album in searchResultsAlbum:
                print()
                print(album['name'])
                for artist in album['artists']:
                    print("Artist: " + artist['name'])
                    print("Artist ID: " + artist['id'])
                print("Album Type: " + album['album_type'])
                print(album['href'])
                print(album['uri'])
                print(album['id'])
                print("Image: " + album['images'][0]['url'])
                print()

        else:
            print()
            print("No Album Results")
            print()

        if searchResultsTrack:
            for track in searchResultsTrack:
                print()
                print(track['name'])
                for artist in track['artists']:
                    print("Artist: " + artist['name'])
                    print("Artist ID: " + artist['id'])
                print("Album: " + track['album']['name'])
                print(track['href'])
                print(track['uri'])
                print(track['id'])
                print()

        else:
            print()
            print("No Album Results")
            print()

    if choice == '0':
        break
# print(json.dumps(VARIABLE, sort_keys = True, indent = 4))
