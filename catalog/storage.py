"""In-memory storage helpers (not part of the public route surface)."""

_STORE = {}


def remember(key, value):
    _STORE[key] = value


def fetch(key, default=None):
    return _STORE.get(key, default)
