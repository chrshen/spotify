import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

def main():
    scope = "user-library-read user-follow-read user-top-read playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlists = sp.user_playlists('cshen330', limit=50)

    track_ids_and_audio_features = dict()

    while playlists:
        for i, playlist in enumerate(playlists['items']):
            if playlist['owner']['id'] == 'cshen330':
                print(playlist['name'])
                tracks = sp.playlist_items(playlist['id'])
                for j, track in enumerate(tracks['items']):
                    if track is not None and track['is_local'] is False:
                        id = track['track']['id']
                        audio_features = sp.audio_features(id)
                        track_ids_and_audio_features.update({id : audio_features})
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    with open('local_data.txt', 'w') as convert_file:
        convert_file.write(json.dumps(track_ids_and_audio_features))


if __name__ == "__main__":
    main()
