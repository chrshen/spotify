import requests

CLIENT_ID = 'a83dd99f76b94da6a263c2a412801031'
CLIENT_SECRET = 'cdf063e674bc4dee85256cfa6a5db765'
AUTH_URL = 'https://accounts.spotify.com/api/token'
USER_ID = 'cshen330'

# PLAYLIST_ID
PLAYLIST_ID = '7CTGQKYCey8L1ZUMQjYxYn'

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# POST to pass access token
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

# saved header for GET requests
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

params = {
    'limit': 50
}

# GET ALl of my playlists
r = requests.get(BASE_URL + 'users/' + USER_ID + '/playlists', headers=headers, params=params)
print(r.status_code)

# convert request to json file
r = r.json()

for playlist in r['items']:
    print(playlist['name'])

