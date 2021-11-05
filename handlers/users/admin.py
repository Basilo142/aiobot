from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
import logging
from for_google_tab.def_for_adding_or_reading import reading_data, adding_data
from keyboards.default import keypad_start, keypad_prihod, keypad_rashod
from loader import dp
from states import AddingData


@dp.message_handler(CommandStart(), user_id=[370912284, 463061743])
async def keyboard_start(message: types.Message):
    await message.answer('Привет {}'.format(message.from_user.full_name), reply_markup=keypad_start)


@dp.message_handler(text='Prihod')
async def key_start_prihod(message: types.Message):
    await message.answer('Тут нужно выбрать от кого поступают средства:', reply_markup=keypad_prihod)


@dp.message_handler(text='Rashod')
async def key_start_rashod(message: types.Message):
    await message.answer('Тут нужно выбрать группу затрат:', reply_markup=keypad_rashod)


@dp.message_handler(text='Info')
async def key_start_info(message: types.Message):
    itog = reading_data(['Ноябрь 2021!B1:B1'])
    spend = reading_data(['Ноябрь 2021!C7:C7'])
    ostatok = reading_data(['Ноябрь 2021!C5:C5'])
    await message.answer('Информация по финансам\n'
                         'за текущий месяц\n'
                         'Итого приход:                     {} грн\n'
                         'Потрачено на сегодня:     {} грн\n'
                         'Остаток:                                {} грн\n'.format(itog, spend, ostatok))


@dp.message_handler(text='Надходження\nАнна', user_id=[463061743])
async def key_prihod_anna(message: types.Message, state: FSMContext):
    old_data = reading_data(['Ноябрь 2021!B2:B2'])
    await message.answer('Укажите сумму поступлений:\n'
                         '(сумма указывается без копеек)\n'
                         'На данный момент в этом поле - {}'.format(old_data))
    await AddingData.D1.set()
    await state.update_data(old_data=old_data)


@dp.message_handler(state=AddingData.D1)
async def adding_anna(message: types.Message, state: FSMContext):
    difference = int(message.text)
    data = await state.get_data()
    old_data = data.get('old_data')
    result = adding_data(['Ноябрь 2021!B2:B2'], difference)
    await message.answer('Значение было изменено\nс {}\n на {}'.format(old_data, result))
    await state.finish()
    await state.reset_state()


@dp.message_handler(text='Надходження\nСаша', user_id=[370912284])
async def key_prihod_sasha(message: types.Message, state: FSMContext):
    old_data = reading_data(['Ноябрь 2021!C2:C2'])
    await message.answer('Укажите сумму поступлений:\n'
                         '(сумма указывается без копеек)\n'
                         'На данный момент в этом поле - {}'.format(old_data))
    await AddingData.D2.set()
    await state.update_data(old_data=old_data)


@dp.message_handler(state=AddingData.D2)
async def adding_sasha(message: types.Message, state: FSMContext):
    difference = int(message.text)
    data = await state.get_data()
    old_data = data.get('old_data')
    result = adding_data(['Ноябрь 2021!C2:C2'], difference)
    await message.answer('Значение было изменено\nс {}\n на {}'.format(old_data, result))
    await state.finish()
    await state.reset_state()


@dp.message_handler(text='🔙 Назад до стартового меню')
async def key_prihod_back(message: types.Message):
    await message.answer(text='Back', reply_markup=keypad_start)
