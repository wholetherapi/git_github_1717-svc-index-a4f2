"""Tiny declarative routing helpers used by the catalog service."""


def route(method, path):
    def decorator(func):
        func.__route__ = (method, path)
        return func
    return decorator


def stable(func):
    func.__intent__ = "stable"
    return func


def experimental(func):
    func.__intent__ = "experimental"
    return func


def deprecated(func):
    func.__intent__ = "deprecated"
    return func


def internal_only(func):
    func.__internal__ = True
    return func
