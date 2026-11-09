import os

from django.core.asgi import get_asgi_application  # type: ignore[reportMissingModuleSource]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zayshop.settings")

application = get_asgi_application()
