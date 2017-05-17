# After an order is created, it is necessary to transmit information about the composition of the order.
# Docs https://triggmine.freshdesk.com/support/solutions/articles/22000186386-3-order-creation-event

from api_operations import Create


class Order(Create):
    def __init__(self, api_key, api_url):
        Create.__init__(self, api_key=api_key,api_url=api_url,event_name= __class__.__name__)

    """
    Cart parameters
    order_id: string (uniq order id in store)
    price_total: double
    qty_total: integer (count of products)
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
    def create(self, order_id, price_total, qty_total, products: list, customer: dict, status):
        return Create._create(self, data=dict(order_id=order_id, price_total=price_total, qty_total=qty_total, products=products, customer=customer, status= status))