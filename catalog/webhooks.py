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


@route("DELETE", "/webhooks/stripe/{subscription_id}")
@deprecated
def delete_stripe_subscription(request):
    """Remove a billing event subscription."""
    return {}


@route("POST", "/internal/webhooks/replay")
@internal_only
def replay_events(request):
    """Replay buffered callbacks (internal operations only)."""
    return {}

