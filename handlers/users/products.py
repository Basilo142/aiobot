from aiogram import types
from aiogram.dispatcher import FSMContext

from for_google_tab import reading_data
from for_google_tab.def_for_adding_or_reading import adding_data
from keyboards.default import (
    keypad_products
)
from loader import dp
from states import AddingData


@dp.message_handler(text='Продукты+хознужды')
async def key_products(message: types.Message):
    await message.answer('Тут треба вибрати конкретніше:', reply_markup=keypad_products)


async def replacement_data(message: types.Message,  state: FSMContext, ranges_old, ranges_plan):
    old_data = reading_data(ranges_old)
    plan_data = reading_data(ranges_plan)
    await message.answer('На сегодняшний день расход составляет - {}\n'
                         'План по данной статье расходов - {}\n'
                         'Укажите сумму потраченную на эту статью расходов:'.format(old_data, plan_data))
    await AddingData.Products.set()
    await state.update_data(old_data=old_data)
    await state.update_data(ranges_old=ranges_old)


@dp.message_handler(state=AddingData.Products)
async def adding_sum(message: types.Message, state: FSMContext):
    difference = int(message.text)
    data = await state.get_data()
    old_data = data.get('old_data')
    ranges_old = data.get('ranges_old')
    result = adding_data(ranges_old, difference)
    await message.answer('Значение было изменено\nс {}\nна {}\nО_о а не много ВЫ едите?))))'.format(old_data, result))
    await state.finish()
    await state.reset_state()


@dp.message_handler(text='Продукты')
async def run(message: types.Message,  state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!O11:O11'], ranges_plan=['Ноябрь 2021!N11:N11'])


@dp.message_handler(text='Кофе')
async def run(message: types.Message,  state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!O12:O12'], ranges_plan=['Ноябрь 2021!N12:N12'])


@dp.message_handler(text='Сладости')
async def run(message: types.Message,  state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!O13:O13'], ranges_plan=['Ноябрь 2021!N13:N13'])


@dp.message_handler(text='Алкоголь')
async def run(message: types.Message,  state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!O14:O14'], ranges_plan=['Ноябрь 2021!N14:N14'])


@dp.message_handler(text='Фрукты')
async def run(message: types.Message,  state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!O15:O15'], ranges_plan=['Ноябрь 2021!N15:N15'])


@dp.message_handler(text='Хоз. нужды')
async def run(message: types.Message,  state: FSMContext):
    await replacement_data(message, state, ranges_old=['Ноябрь 2021!O16:O16'], ranges_plan=['Ноябрь 2021!N16:N16'])

