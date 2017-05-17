# UnitTests of all triggmine events

import unittest
import datetime
from client import Client


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client('YOUR API_URL', 'YOUR API_KEY')

    # Registration event
    def test_registration_success(self):
        response = self.client.registration.create(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                                   device_id_1='465060737', 
                                                   customer_id='1', 
                                                   customer_first_name='Jhon', 
                                                   customer_last_name='Doe', 
                                                   customer_email='Jhon.Doe@example.com', 
                                                   customer_date_created=str(datetime.datetime.now()))
        self.assertEqual(201, response.status_code)
    
    # Diagnostic event
    def test_diagnostic_success(self):
        response = self.client.diagnostic.create(date_created=str(datetime.datetime.now()),
                                                 diagnostic_type="Install_Test_Plugin", description="TestCms", status=1)
        self.assertEqual(201, response.status_code)

    
    # Cart event
    def test_cart_success(self):
        response = self.client.cart.create(order_id="22",price_total="210.86",qty_total="1",
                                        products=[dict(product_id= "421",
                                            product_name= "Elizabeth Knit Top",
                                            product_desc= "Loose fitting from the shoulders, open weave knit top. Semi sheer.  Slips on. Faux button closure detail on the back. Linen/Cotton. Machine wash.",
                                            product_sku= "wbk013",
                                            product_image= "https://1924magento.triggmine.com.ua/media/catalog/product/cache/1/image/265x/9df78eab33525d08d6e5fb8d27136e95/w/b/wbk012t.jpg",
                                            product_url= "https://1924magento.triggmine.com.ua/elizabeth-knit-top-596.html",
                                            product_qty= 1,
                                            product_price= 210,
                                            product_total_val= 210,
                                            product_categories= ['New Arrivals','Tops & Blouses'])],
                                        customer=dict(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                            customer_id='1', 
                                            customer_first_name='Jhon', 
                                            customer_last_name='Doe', 
                                            customer_email='Jhon.Doe@example.com', 
                                            customer_date_created="2016-09-08 10:20:37"))
    # Login event
    def test_login_success(self):
        response = self.client.login.create(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                            device_id_1='465060737', 
                                            customer_id='1', 
                                            customer_first_name='Jhon', 
                                            customer_last_name='Doe', 
                                            customer_email='Jhon.Doe@example.com', 
                                            customer_date_created=str(datetime.datetime.now()))

        self.assertEqual(200, response.status_code)

    # Logout event
    def test_logout_success(self):
        response = self.client.logout.create(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                             device_id_1='465060737', 
                                             customer_id='1', 
                                             customer_first_name='Jhon', 
                                             customer_last_name='Doe', 
                                             customer_email='Jhon.Doe@example.com', 
                                             customer_date_created=str(datetime.datetime.now()))
        self.assertEqual(200, response.status_code)
    
    # History event
    def test_history_success(self):
        response = self.client.history.create(orders= 
                                        [dict(order_id="22",price_total="210.86",qty_total="1",
                                            products=[dict(product_id= "421",
                                                product_name= "Elizabeth Knit Top",
                                                product_desc= "Loose fitting from the shoulders, open weave knit top. Semi sheer.  Slips on. Faux button closure detail on the back. Linen/Cotton. Machine wash.",
                                                product_sku= "wbk013",
                                                product_image= "https://1924magento.triggmine.com.ua/media/catalog/product/cache/1/image/265x/9df78eab33525d08d6e5fb8d27136e95/w/b/wbk012t.jpg",
                                                product_url= "https://1924magento.triggmine.com.ua/elizabeth-knit-top-596.html",
                                                product_qty= 1,
                                                product_price= 210,
                                                product_total_val= 210,
                                                product_categories= ['New Arrivals','Tops & Blouses'])],
                                            customer=dict(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                                customer_id='1', 
                                                customer_first_name='Jhon', 
                                                customer_last_name='Doe', 
                                                customer_email='Jhon.Doe@example.com', 
                                                customer_date_created="2016-09-08 10:20:37")),
                                        dict(order_id="22",price_total="210.86",qty_total="1",
                                            products=[dict(product_id= "421",
                                                product_name= "Elizabeth Knit Top",
                                                product_desc= "Loose fitting from the shoulders, open weave knit top. Semi sheer.  Slips on. Faux button closure detail on the back. Linen/Cotton. Machine wash.",
                                                product_sku= "wbk013",
                                                product_image= "https://1924magento.triggmine.com.ua/media/catalog/product/cache/1/image/265x/9df78eab33525d08d6e5fb8d27136e95/w/b/wbk012t.jpg",
                                                product_url= "https://1924magento.triggmine.com.ua/elizabeth-knit-top-596.html",
                                                product_qty= 1,
                                                product_price= 210,
                                                product_total_val= 210,
                                                product_categories= ['New Arrivals','Tops & Blouses'])],
                                            customer=dict(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                                customer_id='1', 
                                                customer_first_name='Jhon', 
                                                customer_last_name='Doe', 
                                                customer_email='Jhon.Doe@example.com', 
                                                customer_date_created="2016-09-08 10:20:37"))])
        self.assertEqual(200, response.status_code)
        
        # Navigation event
    def test_navigation_success(self):
            response = self.client.navigation.create(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
                                        products=[dict(product_id= "421",
                                            product_name= "Elizabeth Knit Top",
                                            product_desc= "Loose fitting from the shoulders, open weave knit top. Semi sheer.  Slips on. Faux button closure detail on the back. Linen/Cotton. Machine wash.",
                                            product_sku= "wbk013",
                                            product_image= "https://1924magento.triggmine.com.ua/media/catalog/product/cache/1/image/265x/9df78eab33525d08d6e5fb8d27136e95/w/b/wbk012t.jpg",
                                            product_url= "https://1924magento.triggmine.com.ua/elizabeth-knit-top-596.html",
                                            product_qty= 1,
                                            product_price= 210,
                                            product_total_val= 210,
                                            product_categories= ['New Arrivals','Tops & Blouses'])],
                                        customer=dict(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                            customer_id='1', 
                                            customer_first_name='Jhon', 
                                            customer_last_name='Doe', 
                                            customer_email='Jhon.Doe@example.com', 
                                            customer_date_created="2016-09-08 10:20:37"))
            self.assertEqual(201, response.status_code)

        # Order event
    def test_order_success(self):
            response = self.client.order.create(order_id="22",price_total="210.86",qty_total="1",status="Paid",
                                        products=[dict(product_id= "421",
                                            product_name= "Elizabeth Knit Top",
                                            product_desc= "Loose fitting from the shoulders, open weave knit top. Semi sheer.  Slips on. Faux button closure detail on the back. Linen/Cotton. Machine wash.",
                                            product_sku= "wbk013",
                                            product_image= "https://1924magento.triggmine.com.ua/media/catalog/product/cache/1/image/265x/9df78eab33525d08d6e5fb8d27136e95/w/b/wbk012t.jpg",
                                            product_url= "https://1924magento.triggmine.com.ua/elizabeth-knit-top-596.html",
                                            product_qty= 1,
                                            product_price= 210,
                                            product_total_val= 210,
                                            product_categories= ['New Arrivals','Tops & Blouses'])],
                                        customer=dict(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                            customer_id='1', 
                                            customer_first_name='Jhon', 
                                            customer_last_name='Doe', 
                                            customer_email='Jhon.Doe@example.com', 
                                            customer_date_created="2016-09-08 10:20:37"))
            self.assertEqual(201, response.status_code)


if __name__ == '__main__':
    unittest.main()