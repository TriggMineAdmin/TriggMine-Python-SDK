"""
    Your ApiKey && ApiUrl > https://client.triggmine.com.ua/login > Settings > Integration
    api_url = ApiUrl
    api_key = ApiKey

    Api Docs: https://triggmine.freshdesk.com/support/solutions/folders/22000162303
"""

class Client:
    def __init__(self, api_url, api_key):
            self.api_url = api_url
            self.api_key = api_key

	# propertie return registration class instanse with api authorize
    @property
    def registration(self):
        from events.registration import Registration
        return Registration(api_key=self.api_key, api_url=self.api_url)

	# propertie return cart class instanse with api authorize
    @property
    def cart(self):
        from events.cart import Cart
        return Cart(api_key=self.api_key, api_url=self.api_url)

	# propertie return diagnostic class instanse with api authorize
    @property
    def diagnostic(self):
        from events.diagnostic import Diagnostic
        return Diagnostic(api_key=self.api_key, api_url=self.api_url)

	# propertie return history class instanse with api authorize
    @property
    def history(self):
        from events.history import History
        return History(api_key=self.api_key, api_url=self.api_url)

	# propertie return login class instanse with api authorize
    @property
    def login(self):
        from events.login import Login
        return Login(api_key=self.api_key, api_url=self.api_url)

	# propertie return logout class instanse with api authorize
    @property
    def logout(self):
        from events.logout import Logout
        return Logout(api_key=self.api_key, api_url=self.api_url)

	# propertie return navigation class instanse with api authorize
    @property
    def navigation(self):
        from events.navigation import Navigation
        return Navigation(api_key=self.api_key, api_url=self.api_url)

	# propertie return order class instanse with api authorize
    @property
    def order(self):
        from events.order import Order
        return Order(api_key=self.api_key, api_url=self.api_url)


