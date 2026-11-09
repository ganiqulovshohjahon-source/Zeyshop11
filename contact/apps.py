from django.apps import AppConfig  # type: ignore[reportMissingModuleSource]


class ContactConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "contact"
    site_name = "Zay Shop"  # Add this line to define the site name
