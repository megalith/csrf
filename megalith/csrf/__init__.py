from pyramid.events import ContextFound
from pyramid.session import check_csrf_token

def validate_csrf(event):
    request = event.request

    if request.method not in ("GET", "HEAD", "OPTIONS"):
        check_csrf_token(request)

def includeme(config):
    """
    Sets up CSRF validation for the specified configuration.
    """
    config.add_subscriber(validate_csrf, ContextFound)