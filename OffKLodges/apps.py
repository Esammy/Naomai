from django.apps import AppConfig


class OffklodgesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OffKLodges'

    def ready(self):
        import OffKLodges.signals