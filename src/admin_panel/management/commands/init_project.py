"""Module for the management command 'init_project'."""
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from config import settings # noqa

# User = get_user_model()


class Command(BaseCommand):
    """Command for basic data initialization."""

    def handle(self, *args, **options):
        """Handle command."""
        self._create_superuser()

        if settings.DEBUG:
            pass
            # TODO: _create_test_users
            # self._create_test_users()
            # self._create_test_admins() > staff: True

    @staticmethod
    def _create_superuser():
        # TODO: rework for new user model
        pass
