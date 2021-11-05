from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keypad_prihod = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Надходження\nАнна'),
            KeyboardButton(text='Надходження\nСаша')
        ],
        [
            KeyboardButton(text='🔙 Назад до стартового меню')
        ]
    ],
)
