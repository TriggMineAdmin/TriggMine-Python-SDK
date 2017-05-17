"""
Base class for creating events
Your ApiKey && ApiUrl > https://client.triggmine.com.ua/login > Settings > Integration
    api_url = ApiUrl
    api_key = ApiKey
"""

import os
import json
import urllib.parse
from pip._vendor import requests
from sources import get_event_url


class Create:
    def __init__(self, api_key, api_url, event_name):
        self.api_key = api_key 
        self.api_url = api_url 
        self.event_name = event_name

    # send event universal method
    def _create(self, data):
        event_url = get_event_url(event_name=self.event_name)
        try:
            res = requests.post(url=urllib.parse.urljoin(self.api_url, event_url), data=json.dumps(data), headers={'content-type': 'application/json', 'ApiKey': str(self.api_key)})
        except requests.exceptions.RequestException as e:
            print(e)
        return res