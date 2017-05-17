# When the user opens a product card, the information about the product is transmitted.
# Docs https://triggmine.freshdesk.com/support/solutions/articles/22000186390-7-navigation

from api_operations import Create


class Navigation(Create):
    def __init__(self, api_key, api_url):
        Create.__init__(self, api_key=api_key,api_url=api_url,event_name= __class__.__name__)

    """
    Navigation parameters
    user_agent: string (contents of User-Agent header: taken from the current request, if it exists
    products: LIST of products
        "product_id": string ,
        "product_name": string ,
        "product_desc": string ,
        "product_sku": string ,
        "product_image": string ,
        "product_url": string ,
        "product_qty": integer ,
        "product_price": integer ,
        "product_total_val": integer ,
        "product_categories": [
        string,
        string,
        …]
    customer:
        "device_id": string (device hash, can be retrieved from the FingerprintJS library),
        "device_id_1": string (device ID, can be retrieved from the ClientJS library),
        "customer_id": string ,
        "customer_first_name": string ,
        "customer_last_name": string ,
        "customer_email": string ,
        "customer_date_created": string 
    """
    def create(self, user_agent, products: list, customer):
        return Create._create(self, data = dict(user_agent= user_agent, products= products, customer= customer))
