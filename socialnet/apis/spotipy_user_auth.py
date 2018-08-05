import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Please enter username as second arguement.")
    sys.exit()

token = util.prompt_for_user_token(username, scope)