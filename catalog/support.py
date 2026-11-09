"""HTTP routes for the support module."""

from catalog.routes import route, stable, experimental, deprecated, internal_only


@route("GET", "/support/tickets")
@stable
def list_tickets(request):
    """Return the paged list of support tickets."""
    return {}


@route("POST", "/support/tickets")
@stable
def open_ticket(request):
    """Open a new support ticket."""
    return {}


@route("GET", "/support/tickets/{ticket_id}")
@stable
def get_ticket(request):
    """Return a single support ticket by id."""
    return {}


@route("GET", "/internal/support/health")
@internal_only
def health_check(request):
    """Internal liveness probe for the support service."""
    return {}

