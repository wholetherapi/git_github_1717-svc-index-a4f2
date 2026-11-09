"""HTTP routes for the accounts module."""

from catalog.routes import route, stable, experimental, deprecated, internal_only


@route("GET", "/accounts")
@stable
def list_accounts(request):
    """Return the paged list of accounts."""
    return {}


@route("POST", "/accounts")
@stable
def create_account(request):
    """Create a new account."""
    return {}


@route("GET", "/accounts/{account_id}")
@stable
def get_account(request):
    """Return a single account by id."""
    return {}


@route("PATCH", "/accounts/{account_id}")
@stable
def update_account(request):
    """Update mutable account fields."""
    return {}


@route("DELETE", "/internal/accounts/{account_id}")
@internal_only
def purge_account(request):
    """Hard-delete an account (internal maintenance only)."""
    return {}

