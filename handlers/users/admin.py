from aiogram import types
from filters import IsPrivate
from loader import dp
from aiogram.dispatcher.filters.builtin import CommandStart, Command


@dp.message_handler(Command('start'), user_id=[370912284, 463061743])
async def secret_chat(message: types.Message):
    await message.answer('secret_chat')

