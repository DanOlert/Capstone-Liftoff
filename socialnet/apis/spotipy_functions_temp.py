# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util

def CONSOLE_show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print ("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']) )


if __name__ == '__main__':
    print('Hi! Call a function in here')

#NOTE this will become the below function "show_spotify_playlists"
    scope = 'user-library-read'

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print ("Whoops, need your username!")
        print ("usage: python spotipy_functions.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print ()
                print (playlist['name'])
                print ('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                CONSOLE_show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print ("Can't get token for", username)

def show_spotify_playlist(playlist_id):

    return(" ")

def show_spotify_user():
    user = spotifyObject().current_user()
    return user['display_name']
