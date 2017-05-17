# After a successful user registration, the information about the user should be transmitted.
# Docs https://triggmine.freshdesk.com/support/solutions/articles/22000186387-4-new-user-registration

import datetime
from api_operations import Create


class Registration(Create):
    def __init__(self, api_key, api_url):
        Create.__init__(self, api_key=api_key,api_url=api_url,event_name= __class__.__name__)

    """
    Customer registration parameters
    device_id: string (device hash, can be retrieved from the FingerprintJS library),
    device_id_1: string (device ID, can be retrieved from the ClientJS library),
    customer_id: string (uniq customer id in yor system),
    customer_first_name: string (customer first name),
    customer_last_name: string (customer last name),
    customer_email: string (customer email),
    customer_date_created: string (customer registration date)
    """
    def create(self, device_id, device_id_1, customer_id, customer_first_name, customer_last_name, customer_email, customer_date_created = str(datetime.datetime.now())):
        return Create._create(self, data = dict(device_id= device_id, 
                                                device_id_1= device_id_1, 
                                                customer_id= customer_id, 
                                                customer_first_name= customer_first_name, 
                                                customer_last_name= customer_last_name, 
                                                customer_email= customer_email, 
                                                customer_date_created= customer_date_created))
