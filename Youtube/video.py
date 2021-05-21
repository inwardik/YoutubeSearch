import json
import requests
from datetime import datetime

def get_videos_links(params):
    params['key'] = 'AIzaSyAmVfqK9tJKNKcV9ochOOSetUyb_cGKo6Y'
    params['part'] = 'snippet'
    params['maxResults'] = str(params['maxResults'])
    if params.get('publishedAfter'):
        params['publishedAfter'] = params['publishedAfter'].strftime("%Y-%m-%dT%H:%M:%SZ")
    if params.get('publishedBefore'):
        params['publishedBefore'] = params['publishedBefore'].strftime("%Y-%m-%dT%H:%M:%SZ")

    #params['publishedAfter'] = '2021-04-01T00:00:00Z',  # Must be deleted
    if params['location_radius']:
        params['type'] = 'video'
        params['location_radius'] = str(params['location_radius']) + 'km'
    for key, value in params.copy().items():
        if not value:
            del (params[key])
    print(params)
    url = 'https://youtube.googleapis.com/youtube/v3/search'
    r = requests.get(url, params=params)
    resp_dict = json.loads(r.text)
    if resp_dict.get('items'):
        return resp_dict['items']
    return []

