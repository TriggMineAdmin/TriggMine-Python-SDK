"""
    Your ApiKey && ApiUrl > https://client.triggmine.com.ua/login > Settings > Integration
    api_url = ApiUrl
    api_key = ApiKey
"""

class Client:
    def __init__(self, api_url, api_key):
        if api_url is not None:
            self.api_url = api_url
        if api_key is not None:
            self.api_key = api_key

    @property
    def registration(self):
        from events.registration import Registration
        return Registration(api_key=self.api_key, api_url=self.api_url);




client = Client('https://cabinet481950268.triggmine.com/', '7f3d77bc1d8b416fa93a8c119db6d947')
client.registration.create(
    dict(device_id='4c3d48512d48b2603092b5a45ba74c8c', device_id_1='465060737', customer_id='980',
         customer_first_name='Max', customer_last_name='Riabchynskyi', customer_email='mr@triggmine.com',
         customer_date_created='2016-09-08 10:20:37'))