from django.apps import AppConfig


class LoyaltyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loyalty'

    def ready(self) -> None:
        # Import signals if added later
        return super().ready()
