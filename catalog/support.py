"""HTTP routes for the support module."""

from catalog.routes import route, stable, experimental, deprecated, internal_only


@route("GET", "/support/tickets")
@stable
def list_tickets(request):
    """Return the paged list of support tickets."""
    return {}


@route("GET", "/support/tickets/{ticket_id}")
@stable
def get_ticket(request):
    """Return a single support ticket by id."""
    return {}


@route("POST", "/support/tickets/{ticket_id}/assign")
@stable
def assign_ticket(request):
    """Assign a support ticket to an agent."""
    return {}


@route("POST", "/support/tickets/bulk-close")
@stable
def bulk_close_tickets(request):
    """Close a batch of support tickets."""
    raise NotImplementedError("Route handler is not implemented yet")


@route("GET", "/internal/support/health")
@internal_only
def health_check(request):
    """Internal liveness probe for the support service."""
    return {}

