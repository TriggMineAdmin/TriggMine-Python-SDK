# TriggMine-Python-SDK
## Description
TriggMine is an automated email marketing platform, tailored to the eCommerce needs. We've harnessed the power of behavioral-based email workflows! In real time, our system automatically tracks customers behavior and separates them into highly relevant, behavior-focused segments and sends them highly personalized emails.
It takes less than 30 minutes to launch fully automated email campaign! Now marketers can finally watch your email open rates, clicks and sales sky rocket, without hiring tech experts or touching a single line of code!
TriggMine web site: http://www.triggmine.com/

## How-to
TriggMine API сan take 8 types of events. All events models send through SendEvent method which has static and async versions.

#### Event list 
**Event type** |
Registration |
Cart |
History |
Login |
Logout |
Navigation |
Order |
Diagnostic |

### Example
#### Configure your client
```Python
from client import Client
client = Client('YOUR API_URL', 'YOUR API_KEY')
```

#### Send events
```Python
# Registration event example
response = self.client.registration.create(device_id='4c3d48512d48b2603092b5a45ba74c8c', 
                                                   device_id_1='465060737', 
                                                   customer_id='1', 
                                                   customer_first_name='Jhon', 
                                                   customer_last_name='Doe', 
                                                   customer_email='Jhon.Doe@example.com', 
                                                   customer_date_created=str(datetime.datetime.now()))

# Diagnostic event example
response = client.diagnostic.create(date_created=str(datetime.datetime.now()),
                                                 diagnostic_type="Install_Test_Plugin", description="TestCms", status=1)
```

### API Docs
Detail information about TriggMine API you can find [here](https://triggmine.freshdesk.com/support/solutions/folders/22000162303)
 
