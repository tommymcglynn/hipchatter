import requests
import json

def get_joke():
    r = requests.get('http://api.icndb.com/jokes/random')
    response = json.loads(r.text)
    if response.get('type') == 'success':
        return response.get('value').get('joke')

    return None
