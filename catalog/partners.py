"""HTTP routes for the partners module."""

from catalog.routes import route, stable, experimental, deprecated, internal_only


@route("GET", "/partners")
@stable
def list_partners(request):
    """Return the paged list of channel partners."""
    return {}


@route("POST", "/partners")
@experimental
def create_partner(request):
    """Register a new channel partner."""
    return {}


@route("GET", "/partners/{partner_id}")
@stable
def get_partner(request):
    """Return a single partner by id."""
    return {}

