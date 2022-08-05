"""Handlers initialization."""

from aiogram import types
from aiogram.dispatcher import FSMContext
from .loader import bot, dp


@dp.message_handler(commands=['start'], state='*')
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.chat.id, 'Работает')




