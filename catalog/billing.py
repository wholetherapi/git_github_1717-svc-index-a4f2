"""HTTP routes for the billing module."""

from catalog.routes import route, stable, experimental, deprecated, internal_only


@route("GET", "/billing/invoices")
@stable
def list_invoices(request):
    """Return the paged list of invoices."""
    return {}


@route("POST", "/billing/invoices")
@experimental
def create_invoice(request):
    """Create a new invoice."""
    return {}


@route("GET", "/billing/invoices/{invoice_id}")
@stable
def get_invoice(request):
    """Return a single invoice by id."""
    return {}


@route("POST", "/billing/invoices/{invoice_id}/void")
@deprecated
def void_invoice(request):
    """Void an issued invoice."""
    return {}

