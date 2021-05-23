import json
import requests


def get_videos_links(params):
    params['key'] = 'AIzaSyAmVfqK9tJKNKcV9ochOOSetUyb_cGKo6Y'
    params['part'] = 'snippet'
    params['maxResults'] = str(params['maxResults'])
    if params.get('publishedAfter'):
        params['publishedAfter'] = params['publishedAfter'].strftime("%Y-%m-%dT%H:%M:%SZ")
    if params.get('publishedBefore'):
        params['publishedBefore'] = params['publishedBefore'].strftime("%Y-%m-%dT%H:%M:%SZ")
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

#https://youtube.googleapis.com/youtube/v3/videos?part=statistics&id=bh9Txxt8z2M&key=AIzaSyAmVfqK9tJKNKcV9ochOOSetUyb_cGKo6Y
#https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyAmVfqK9tJKNKcV9ochOOSetUyb_cGKo6Y&textFormat=plainText&part=snippet&videoId=l3Px1lru8OI&maxResults=50
