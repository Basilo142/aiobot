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
    ],
    # resize_keyboard=True,
    # one_time_keyboard=True
    input_field_placeholder='Hello World'
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
    ],
    # resize_keyboard=True,
    input_field_placeholder='check_payment'
)
