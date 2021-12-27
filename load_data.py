import spotipy
from spotipy.oauth2 import SpotifyOAuth
import numpy as np

# THIS USES THE SPOPTIPY LIBRARY

def main():
    scope = "user-library-read user-follow-read user-top-read playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    train_playlist = sp.playlist_items(playlist_id="7CTGQKYCey8L1ZUMQjYxYn")

    length = train_playlist['total']

    labels = [ "popularity", "explicit", "duration_ms", "danceability", "energy",
              "key", "loudness", "mode", "speechiness", "acousticness"]

    train_data = np.ndarray(shape=(length, len(labels)))

    # for i, label in enumerate(labels):
    #   np.put_along_axis(train_data, np.array([[i]]), label, axis=0)

    while train_playlist:
        for i, item in enumerate(train_playlist['items']):
            track = item['track']

            """
            train_data.put((i, 0), track['popularity'])
            train_data.put((i, 1), track['explicit'])
            train_data.put((i, 2), track['duration_ms'])
            train_data.put((i, 3), features['danceability'])
            train_data.put((i, 4), track['energy'])
            train_data.put((i, 5), track['key'])
            train_data.put((i, 6), track['loudness'])
            train_data.put((i, 7), track['mode'])
            train_data.put((i, 8), track['speechiness'])
            train_data.put((i, 9), track['acousticness'])
            """

            print("%4d %s %s" % (i + 1 + train_playlist['offset'], track['artists'], track['name']))
        if train_playlist['next']:
            train_playlist = sp.next(train_playlist)
        else:
            train_playlist = None


if __name__ == "__main__":
    main()
