import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text, CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from for_google_tab import reading_data
from for_google_tab.def_for_adding_or_reading import adding_data
from keyboards.default import gogo, check_payment, keypad_start, keypad_prihod, keypad_rashod, keypad_permanent_spending
from keyboards.inline.callback_data import buy_callback
from keyboards.inline.key_inline import inline_buttons, drugaya_key
from loader import dp
from states import AddingData


@dp.message_handler(text='Обязательные/постоянные')
async def key_rashod_permanent(message: types.Message):
    await message.answer('Тут треба вібрати конкретніше:', reply_markup=keypad_permanent_spending)


# @dp.message_handler(text='Квартплата')
async def key_kvarplata(message: types.Message,  state: FSMContext, ranges_old, ranges_plan):
    old_data = reading_data(ranges_old)
    plan_data = reading_data(ranges_plan)
    await message.answer('На сегодняшний день расход составляет - {}\n'
                         'План по данной статье расходов - {}\n'
                         'Укажите сумму потраченную на эту статью расходов:'.format(old_data, plan_data))
    await AddingData.Kvarplata.set()
    await state.update_data(old_data=old_data)
    await state.update_data(ranges_old=ranges_old)


@dp.message_handler(state=AddingData.Kvarplata)
async def adding_kvarplata(message: types.Message, state: FSMContext):
    difference = int(message.text)
    data = await state.get_data()
    old_data = data.get('old_data')
    ranges_old = data.get('ranges_old')
    result = adding_data(ranges_old, difference)
    await message.answer('Значение было *** изменено\nс {}\n на {}'.format(old_data, result))
    await state.finish()
    await state.reset_state()


@dp.message_handler(text='Квартплата')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C12:C12'], ranges_plan=['Ноябрь 2021!B12:B12'])


@dp.message_handler(text='Взнос в класс Соне')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C11:C11'], ranges_plan=['Ноябрь 2021!B11:B11'])


@dp.message_handler(text='Аренда')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C13:C13'], ranges_plan=['Ноябрь 2021!B13:B13'])


@dp.message_handler(text='Бензин Саша')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C14:C14'], ranges_plan=['Ноябрь 2021!B14:B14'])


@dp.message_handler(text='Проезд Аня')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C15:C15'], ranges_plan=['Ноябрь 2021!B15:B15'])


@dp.message_handler(text='Долг Аня')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C16:C16'], ranges_plan=['Ноябрь 2021!B16:B16'])


@dp.message_handler(text='Долг Саша')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C17:C17'], ranges_plan=['Ноябрь 2021!B17:B17'])


@dp.message_handler(text='Соне на обеды')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C19:C19'], ranges_plan=['Ноябрь 2021!B19:B19'])


@dp.message_handler(text='Обеды Аня')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C20:C20'], ranges_plan=['Ноябрь 2021!B20:B20'])


@dp.message_handler(text='Обеды Саша')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C21:C21'], ranges_plan=['Ноябрь 2021!B21:B21'])


@dp.message_handler(text='Мобильный Соня')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C22:C22'], ranges_plan=['Ноябрь 2021!B22:B22'])


@dp.message_handler(text='Мобильный Саша')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C23:C23'], ranges_plan=['Ноябрь 2021!B23:B23'])


@dp.message_handler(text='Мобильный Степан')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C24:C24'], ranges_plan=['Ноябрь 2021!B24:B24'])


@dp.message_handler(text='Мобильный Анна')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C25:C25'], ranges_plan=['Ноябрь 2021!B25:B25'])


@dp.message_handler(text='Youtube')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C26:C26'], ranges_plan=['Ноябрь 2021!B26:B26'])


@dp.message_handler(text='Spotify')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C27:C27'], ranges_plan=['Ноябрь 2021!B27:B27'])


@dp.message_handler(text='Интернет')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C28:C28'], ranges_plan=['Ноябрь 2021!B28:B28'])


@dp.message_handler(text='Обеды в школу')
async def runn(message: types.Message,  state: FSMContext):
    await key_kvarplata(message, state, ranges_old=['Ноябрь 2021!C18:C18'], ranges_plan=['Ноябрь 2021!B18:B18'])





















# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=gogo)


# @dp.message_handler(Command('gogo'))
# async def bot_start(message: types.Message):
#     await message.answer(f"gogo, {message.from_user.full_name}!", reply_markup=gogo)


@dp.message_handler(Command('inline'))
async def inline_button(messasge: types.Message):
    await messasge.answer(text='Выбери что тебе нужно :\n'
                          'вот варианты: \n', reply_markup=inline_buttons)


@dp.callback_query_handler(buy_callback.filter(item='1_first_inline'))
async def ff(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info('*** i tak callback - {}'.format(call.data))
    logging.info('*** i tak callback_dict - {}'.format(callback_data))
    await call.message.answer('*** i tak callback - {}'.format(call.data))
    await call.message.answer('*** i tak callback_dict - {}'.format(callback_data),
                              reply_markup=drugaya_key)


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('отмена', show_alert=True)
    await call.message.edit_reply_markup()

