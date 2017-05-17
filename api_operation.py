"""
base class for creating events
"""

import os
import requests
import json
from sources import get_event_url


class Create:
    def __init__(self, api_key, api_url, event_name):
        self.api_key = api_key,
        self.api_url = api_url
        self.event_name = event_name

    # send event universal method
    def create(self, data):
        event_url = get_event_url(event_name=self.event_name)
        try:
            response = requests.post(url=os.path.join(self.api_url, event_url), data=json.dumps(data)
                                     , headers={'content-type': 'application/json', 'ApiKey': self.api_key})
        except requests.exceptions.RequestException as e:
            print(e)
        return response
