from django.apps import AppConfig


class EventureSettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventureApp'

# Signal handlers
    def ready(self):
        from .models import models  # Signals module in models.py
