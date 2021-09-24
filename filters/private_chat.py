from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsPrivate(BoundFilter):
    async def check(self, massage: types.Message) -> bool:
        return massage.chat.type == types.ChatType.PRIVATE
        # return massage.text == '/start'