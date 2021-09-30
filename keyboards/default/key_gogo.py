from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gogo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='first but')
        ],
        [
            KeyboardButton(text='Prihod'),
            KeyboardButton(text='Rashod')
        ],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True
    input_field_placeholder='Hello World'
)
