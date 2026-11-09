"""HTTP routes for the reports module."""

from catalog.routes import route, stable, experimental, deprecated, internal_only


@route("GET", "/reports/monthly")
@stable
def monthly_report(request):
    """Return the monthly usage report."""
    raise NotImplementedError("Route handler is not implemented yet")


@route("GET", "/reports/daily")
@deprecated
def daily_report(request):
    """Return the daily usage report."""
    return {}


@route("GET", "/reports/weekly")
@stable
def weekly_report(request):
    """Return the weekly usage report."""
    return {}

