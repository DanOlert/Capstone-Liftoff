import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

scope = 'user-library-read'

#TODO make this a function that can be called rather than a console command
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Please enter username as second arguement.")
    sys.exit()

token = util.prompt_for_user_token(username, scope)

#TODO this doesnt work again, because it can't find my cashed username
def getSpotifyToken(username, scope):
    #TODO put these secret keys in another file
    try:
        token = util.prompt_for_user_token(username, scope, client_id="284e9c8ac07046ac9e1443a4ab3bb4df", client_secret="04b6434d9afd4197a9f1da648429daee", redirect_uri="https://google.com/")
    except:
        os.remove(f".cashe-{username}")
        token = util.prompt_for_user_token(username, scope, client_id="284e9c8ac07046ac9e1443a4ab3bb4df", client_secret="04b6434d9afd4197a9f1da648429daee", redirect_uri="https://google.com/")
    #TODO if token check!
    return(token)
