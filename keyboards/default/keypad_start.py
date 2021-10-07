from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keypad_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Prihod'),
            KeyboardButton(text='Rashod')
        ],
        [
            KeyboardButton(text='Info')
        ]

    ],
)
