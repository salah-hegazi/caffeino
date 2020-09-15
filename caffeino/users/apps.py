from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "caffeino.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import caffeino.users.signals  # noqa F401
        except ImportError:
            pass
