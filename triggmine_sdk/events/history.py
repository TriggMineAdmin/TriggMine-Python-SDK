# Module configuration on the resource side should allow to produce export of orders within a specified time range - FROM and TILL the established date.
# https://triggmine.freshdesk.com/support/solutions/articles/22000186391-8-order-history-export

from api_operations import Create


class History(Create):
    def __init__(self, api_key, api_url):
        Create.__init__(self, api_key=api_key,api_url=api_url,event_name= __class__.__name__)

    """
    History event its List of orders. (events.order.py)
    """
    def create(self, orders: list):
        return Create._create(self, data = dict(orders= orders))
