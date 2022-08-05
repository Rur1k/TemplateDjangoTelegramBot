"""Application initialization."""

from django.apps import AppConfig


class TgBotConfig(AppConfig):
    """Class initialization."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "src.tg_bot"
