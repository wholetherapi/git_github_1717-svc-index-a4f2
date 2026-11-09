"""HTTP routes for the webhooks module."""

from catalog.routes import route, stable, experimental, deprecated, internal_only


@route("POST", "/webhooks/github")
@stable
def github_webhook(request):
    """Receive repository event callbacks."""
    return {}


@route("POST", "/webhooks/stripe")
@experimental
def stripe_webhook(request):
    """Receive billing event callbacks."""
    return {}

