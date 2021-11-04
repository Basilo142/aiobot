from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keypad_rashod = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Обязательные/постоянные'),
        ],
        [
            KeyboardButton(text='Продукты+хознужды'),
        ],
        [
            KeyboardButton(text='Отдых'),
        ],
        [
            KeyboardButton(text='Здоровье/спорт'),
        ],
        [
            KeyboardButton(text='Красота'),
        ],
        [
            KeyboardButton(text='Одежда'),
        ],
        [
            KeyboardButton(text='Другое'),
        ],
        [
            KeyboardButton(text='Назад до стартового меню')
        ]
    ],
)
