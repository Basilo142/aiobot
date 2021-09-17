from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp


@dp.message_handler(Command)
async def bot_start(message: types.Message):
    await message.answer(f"gogo, {message.from_user.full_name}!")
