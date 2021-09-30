from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand('test', 'go test'),
            types.BotCommand('gogo', 'gogo'),
            types.BotCommand('inline', 'inline Button'),
        ]
    )
