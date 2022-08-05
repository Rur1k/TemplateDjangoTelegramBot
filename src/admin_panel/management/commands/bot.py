"""String telegram bot."""
from django.core.management.base import BaseCommand


async def on_startup(dp):
    """Process start middleware."""
    import src.tg_bot.middlewares  # noqa

    src.tg_bot.middlewares.setup(dp)


class Command(BaseCommand):
    """Class base start bot."""

    def handle(self, *args, **options):
        """Process initialization handlers."""
        from aiogram import executor

        import src.tg_bot.handlers  # noqa
        from src.tg_bot.loader import dp  # noqa

        executor.start_polling(dp, on_startup=on_startup)
