from django.apps import AppConfig


class BokstaeverConfig(AppConfig):
    name = "bokstaever"

    def ready(self):
        import bokstaever.signals  # noqa
