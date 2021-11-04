from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gogo = ReplyKeyboardMarkup(
    keyboard=[
        # [
        #     KeyboardButton(text='Prihod')
        # ],
        [
            KeyboardButton(text='Prihod'),
            KeyboardButton(text='Rashod')
        ],
    ]
)
check_payment = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Приход денег'),
            KeyboardButton(text='Расход денег')
        ],
        [
            KeyboardButton(text='Back')
        ],
    ]
)
