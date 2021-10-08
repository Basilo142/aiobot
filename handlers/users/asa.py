import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text, CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from for_google_tab import reading_data
from keyboards.default import gogo, check_payment, keypad_start, keypad_prihod, keypad_rashod, keypad_permanent_spending
from keyboards.inline.callback_data import buy_callback
from keyboards.inline.key_inline import inline_buttons, drugaya_key
from loader import dp
from states import AddingData


@dp.message_handler(text='Обязательные/постоянные')
async def key_rashod_permanent(message: types.Message):
    await message.answer('Тут треба вібрати конкретніше:', reply_markup=keypad_permanent_spending)


@dp.message_handler(text='Квартплата')
async def key_kvarplata(message: types.Message,  state: FSMContext):
    old_data = reading_data(['Октябрь с 6.10!C12:C12'])
    plan_data = reading_data(['Октябрь с 6.10!B12:B12'])
    await message.answer('На сегодняшний день расход составляет - {}\n'
                         'План по данной статье расходов - {}\n'
                         'Укажите сумму потраченную на эту статью расходов:'.format(old_data, plan_data))
    # await AddingData.D1.set()



# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=gogo)


# @dp.message_handler(Command('gogo'))
# async def bot_start(message: types.Message):
#     await message.answer(f"gogo, {message.from_user.full_name}!", reply_markup=gogo)

#
# @dp.message_handler(text='Rashod')
# async def answer_first(message: types.Message):
#     logging.info('вы нажали первую кнопку-{}'.format(message))
#     await message.answer('вы нажали первую кнопку', reply_markup=check_payment)
#
#
# @dp.message_handler(text='Back')
# async def answer_first(message: types.Message):
#     logging.info('вы нажали Back-{}'.format(message))
#     await message.answer('вы нажали первую кнопку', reply_markup=gogo)
#
#
# @dp.message_handler(Text(equals=['Prihod']))
# async def answer_second(message: types.Message):
#     await message.answer('FUCK_OFF - {}'.format(message.text), reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message_handler(Command('inline'))
# async def inline_button(messasge: types.Message):
#     await messasge.answer(text='Выбери что тебе нужно :\n'
#                           'вот варианты: \n', reply_markup=inline_buttons)
#
#
# @dp.callback_query_handler(buy_callback.filter(item='1_first_inline'))
# async def ff(call: CallbackQuery, callback_data: dict):
#     await call.answer(cache_time=60)
#     logging.info('*** i tak callback - {}'.format(call.data))
#     logging.info('*** i tak callback_dict - {}'.format(callback_data))
#     await call.message.answer('your chose - {}'.format(callback_data.get('name')),
#                               reply_markup=drugaya_key)
#
#
# @dp.callback_query_handler(text='cancel')
# async def cancel(call: CallbackQuery):
#     await call.answer('отмена', show_alert=True)
#     await call.message.edit_reply_markup()
#
