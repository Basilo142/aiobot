import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text, CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from for_google_tab import reading_data
from for_google_tab.def_for_adding_or_reading import adding_data, adding_other
from keyboards.default import (
    gogo, check_payment, keypad_start, keypad_prihod, keypad_rashod, keypad_permanent_spending, keypad_to_rest,
    keypad_health_sports, keypad_the_beauty, keypad_clothes, keypad_other
)
from keyboards.inline.callback_data import buy_callback
from keyboards.inline.key_inline import inline_buttons, drugaya_key
from loader import dp
from states import AddingData


@dp.message_handler(text='Обязательные/постоянные')
async def key_rashod_permanent(message: types.Message):
    await message.answer('Тут треба вибрати конкретніше:', reply_markup=keypad_permanent_spending)


@dp.message_handler(text='Отдых')
async def key_keypad_to_rest(message: types.Message):
    await message.answer('Тут треба вибрати конкретніше:', reply_markup=keypad_to_rest)


@dp.message_handler(text='Здоровье/спорт')
async def key_keypad_health_sports(message: types.Message):
    await message.answer('Тут треба вибрати конкретніше:', reply_markup=keypad_health_sports)


@dp.message_handler(text='Красота')
async def key_keypad_the_beauty(message: types.Message):
    await message.answer('Тут треба вибрати конкретніше:', reply_markup=keypad_the_beauty)


@dp.message_handler(text='Одежда')
async def key_keypad_clothes(message: types.Message):
    await message.answer('Тут треба вибрати конкретніше:', reply_markup=keypad_clothes)


@dp.message_handler(text='Другое')
async def key_keypad_other(message: types.Message):
    await message.answer('Тут треба вибрати конкретніше:', reply_markup=keypad_other)


async def replacement_data(message: types.Message, state: FSMContext, ranges_old, ranges_plan):
    old_data = reading_data(ranges_old)
    plan_data = reading_data(ranges_plan)
    await message.answer('На сегодняшний день расход составляет - {}\n'
                         'План по данной статье расходов - {}\n'
                         'Укажите сумму потраченную на эту статью расходов:'.format(old_data, plan_data))
    await AddingData.Kvarplata.set()
    await state.update_data(old_data=old_data)
    await state.update_data(ranges_old=ranges_old)


@dp.message_handler(state=AddingData.Kvarplata)
async def adding(message: types.Message, state: FSMContext):
    difference = int(message.text)
    data = await state.get_data()
    old_data = data.get('old_data')
    ranges_old = data.get('ranges_old')
    result = adding_data(ranges_old, difference)
    await message.answer('Значение было *** изменено\nс {}\n на {}'.format(old_data, result))
    await state.finish()
    await state.reset_state()


@dp.message_handler(text='Квартплата')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C12:C12'], ranges_plan=['Ноябрь 2021!B12:B12'])


@dp.message_handler(text='Взнос в класс Соне')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C11:C11'], ranges_plan=['Ноябрь 2021!B11:B11'])


@dp.message_handler(text='Аренда')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C13:C13'], ranges_plan=['Ноябрь 2021!B13:B13'])


@dp.message_handler(text='Бензин Саша')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C14:C14'], ranges_plan=['Ноябрь 2021!B14:B14'])


@dp.message_handler(text='Проезд Аня')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C15:C15'], ranges_plan=['Ноябрь 2021!B15:B15'])


@dp.message_handler(text='Долг Аня')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C16:C16'], ranges_plan=['Ноябрь 2021!B16:B16'])


@dp.message_handler(text='Долг Саша')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C17:C17'], ranges_plan=['Ноябрь 2021!B17:B17'])


@dp.message_handler(text='Соне на обеды')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C19:C19'], ranges_plan=['Ноябрь 2021!B19:B19'])


@dp.message_handler(text='Обеды Аня')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C20:C20'], ranges_plan=['Ноябрь 2021!B20:B20'])


@dp.message_handler(text='Обеды Саша')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C21:C21'], ranges_plan=['Ноябрь 2021!B21:B21'])


@dp.message_handler(text='Мобильный Соня')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C22:C22'], ranges_plan=['Ноябрь 2021!B22:B22'])


@dp.message_handler(text='Мобильный Саша')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C23:C23'], ranges_plan=['Ноябрь 2021!B23:B23'])


@dp.message_handler(text='Мобильный Степан')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C24:C24'], ranges_plan=['Ноябрь 2021!B24:B24'])


@dp.message_handler(text='Мобильный Анна')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C25:C25'], ranges_plan=['Ноябрь 2021!B25:B25'])


@dp.message_handler(text='Youtube')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C26:C26'], ranges_plan=['Ноябрь 2021!B26:B26'])


@dp.message_handler(text='Spotify')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C27:C27'], ranges_plan=['Ноябрь 2021!B27:B27'])


@dp.message_handler(text='Интернет')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C28:C28'], ranges_plan=['Ноябрь 2021!B28:B28'])


@dp.message_handler(text='Обеды в школу')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!C18:C18'], ranges_plan=['Ноябрь 2021!B18:B18'])


# ----------------------------------------------------------------------------------------------------------------------


@dp.message_handler(text='Кафе')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!F11:F11'], ranges_plan=['Ноябрь 2021!G11:G11'])


@dp.message_handler(text='Кино')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!F12:F12'], ranges_plan=['Ноябрь 2021!G12:G12'])


# ----------------------------------------------------------------------------------------------------------------------


@dp.message_handler(text='Трени Аня')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!J11:J11'], ranges_plan=['Ноябрь 2021!K11:K11'])


@dp.message_handler(text='Трени Степа')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!J12:J12'], ranges_plan=['Ноябрь 2021!K12:K12'])


@dp.message_handler(text='Трени Саша')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!J13:J13'], ranges_plan=['Ноябрь 2021!K13:K13'])


@dp.message_handler(text='Трени Соня')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!J14:J14'], ranges_plan=['Ноябрь 2021!K14:K14'])


@dp.message_handler(text='Коктейль')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!J15:J15'], ranges_plan=['Ноябрь 2021!K15:K15'])


# ----------------------------------------------------------------------------------------------------------------------


@dp.message_handler(text='Одежда Аня')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!S11:S11'], ranges_plan=['Ноябрь 2021!R11:R11'])


@dp.message_handler(text='Одежда Саша')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!S12:S12'], ranges_plan=['Ноябрь 2021!R12:R12'])


@dp.message_handler(text='Одежда Соня')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!S13:S13'], ranges_plan=['Ноябрь 2021!R13:R13'])


@dp.message_handler(text='Одежда Степан')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!S14:S14'], ranges_plan=['Ноябрь 2021!R14:R14'])


# ----------------------------------------------------------------------------------------------------------------------


@dp.message_handler(text='Маникюр')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!W11:W11'], ranges_plan=['Ноябрь 2021!V11:V11'])


@dp.message_handler(text='брови')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!W12:W12'], ranges_plan=['Ноябрь 2021!V12:V12'])


@dp.message_handler(text='краска')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!W13:W13'], ranges_plan=['Ноябрь 2021!V13:V13'])


@dp.message_handler(text='депиляшка')
async def run(message: types.Message, state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!W14:W14'], ranges_plan=['Ноябрь 2021!V14:V14'])


# ----------------------------------------------------------------------------------------------------------------------


@dp.message_handler(text='Что-то совсем другое)')
async def run(message: types.Message, state: FSMContext):
    await message.answer('Укажи на что портачино (text):')
    await AddingData.OtherText.set()


@dp.message_handler(state=AddingData.OtherText)
async def other_text(message: types.Message, state: FSMContext):
    text = str(message.text)
    await state.update_data(text=text)
    await message.answer('Была указана следующая статья: \n"{}"'.format(text))
    await message.answer('Теперь укажите сумму (грн):')
    await AddingData.OtherInt.set()


@dp.message_handler(state=AddingData.OtherInt)
async def other_int(message: types.Message, state: FSMContext):
    amount = int(message.text)
    data = await state.get_data()
    text = data.get('text')
    adding_other(text, amount)
    await message.answer('Внесенны следующие данные \nстатья расхода - {}\nсумма - {}'.format(text, amount))
    await state.reset_state()





