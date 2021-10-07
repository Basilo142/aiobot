from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command('menu'))
async def show_menu():
    pass