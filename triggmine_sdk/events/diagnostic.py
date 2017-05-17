# While deploying a module, self-check must be done on the side of the resource; this will give the information about the resource.
# Docs https://triggmine.freshdesk.com/support/solutions/articles/22000186383-1-module-installation-event-api-client-

from api_operations import Create


class Diagnostic(Create):
    def __init__(self, api_key, api_url):
        Create.__init__(self, api_key=api_key,api_url=api_url,event_name= __class__.__name__)
    
    """
    Diagnostic parameters
    date_created : string,
    diagnostic_type : string (diagnostic type),
    description : string (diagnostic result),
    status : integer (diagnostic result 1 or 0)
    """
    def create(self, date_created, diagnostic_type, description, status):
        return Create._create(self, data=dict(date_created=date_created, diagnostic_type=diagnostic_type, description=description, status=status))