from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.utils.deep_linking import get_start_link
from filters import IsPrivate
from loader import dp


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    # link = await get_start_link(payload='123123')
    # await message.answer(link)
