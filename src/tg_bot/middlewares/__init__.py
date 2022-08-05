"""Basic initialization file."""

from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    """Middleware connection."""
    dp.middleware.setup(ThrottlingMiddleware())

