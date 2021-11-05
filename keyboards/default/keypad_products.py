from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keypad_products = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Продукты'),
        ], [
            KeyboardButton(text='Кофе'),
        ], [
            KeyboardButton(text='Сладости'),
        ], [
            KeyboardButton(text='Алкоголь'),
        ], [
            KeyboardButton(text='Фрукты'),
        ], [
            KeyboardButton(text='Хоз. нужды'),
        ], [
            KeyboardButton(text='🔙 Назад до стартового меню')
        ]
    ], one_time_keyboard=True
)

keypad_to_rest = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='☕️🍩 Кафе ☕️🍩'),
        ], [
            KeyboardButton(text='🎞 Кино 🎞'),
        ], [
            KeyboardButton(text='🔙 Назад до стартового меню')
        ]
    ], one_time_keyboard=True
)

keypad_health_sports = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🤸🏼 Трени Аня 🤸🏼'),
        ], [
            KeyboardButton(text='🤼‍♂️ Трени Степа 🤼‍♂️'),
        ], [
            KeyboardButton(text='🏋🏻‍♂️ Трени Саша 🏋🏻‍♂️'),
        ], [
            KeyboardButton(text='🧘🏻‍♂️ Трени Соня 🧘🏻‍♂️'),
        ], [
            KeyboardButton(text='🥛 Коктейль 🥛'),
        ], [
            KeyboardButton(text='🔙 Назад до стартового меню')
        ]
    ], one_time_keyboard=True
)

keypad_clothes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Одежда Аня'),
        ], [
            KeyboardButton(text='Одежда Саша'),
        ], [
            KeyboardButton(text='Одежда Соня'),
        ], [
            KeyboardButton(text='Одежда Степан'),
        ], [
            KeyboardButton(text='🔙 Назад до стартового меню')
        ]
    ], one_time_keyboard=True
)

keypad_the_beauty = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Маникюр'),
        ], [
            KeyboardButton(text='брови'),
        ], [
            KeyboardButton(text='краска'),
        ], [
            KeyboardButton(text='депиляшка'),
        ], [
            KeyboardButton(text='🔙 Назад до стартового меню')
        ]
    ], one_time_keyboard=True
)


keypad_other = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Что-то совсем другое)'),
        ], [
            KeyboardButton(text='🔙 Назад до стартового меню')
        ]
    ], one_time_keyboard=True
)


