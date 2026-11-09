from datetime import datetime


def global_context(request):
    """Return global variables for all templates."""
    return {
        "site_name": "Zay Shop",
        "current_year": datetime.now().year,
    }


def global_site_name(request):
    """Backward-compatible alias for the global template context."""
    return global_context(request)
