# API Versioning utilities for Sinai OS

_api_metadata = {}


def api_version(version: str):
    """Decorator to mark API endpoints with version information."""

    def decorator(func):
        # Store metadata in a global dict to avoid setattr on function
        func_id = id(func)
        _api_metadata[func_id] = {
            "version": version,
            "path": getattr(func, "__name__", ""),
            "kwargs": {},
        }
        return func

    return decorator


def get_api_version(func):
    """Get the API version for a function."""
    return _api_metadata.get(id(func), {}).get("version")


def get_api_path(func):
    """Get the API path for a function."""
    return _api_metadata.get(id(func), {}).get("path")


def get_api_kwargs(func):
    """Get the API kwargs for a function."""
    return _api_metadata.get(id(func), {}).get("kwargs")
