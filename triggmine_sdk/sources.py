"""
Base dictionary with triggmine api urls
Function check type of request data and return required event url
"""


def get_event_url(event_name):
    api_events = dict(Cart='api/events/cart',
                      History='api/events/history',
                      Login='api/events/prospect/login',
                      Logout='api/events/prospect/logout',
                      Navigation='api/events/navigation',
                      Order='api/events/order',
                      Registration='api/events/prospect/registration',
                      Diagnostic='control/api/plugin/onDiagnosticInformationUpdated')

    return api_events[event_name]

