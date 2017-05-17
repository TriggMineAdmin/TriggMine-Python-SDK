from api_operation import Create


class Registration(Create):
    def __init__(self, api_key, api_url):
        Create.__init__(api_key=api_url,api_url=api_key,event_name= __class__.__name__)
