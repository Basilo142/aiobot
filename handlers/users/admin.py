from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import keypad_start, keypad_prihod, keypad_rashod
from loader import dp


@dp.message_handler(CommandStart(), user_id=[370912284, 463061743])
async def keyboard_start(message: types.Message):
    await message.answer('Привіт {}'.format(message.from_user.full_name), reply_markup=keypad_start)


@dp.message_handler(text='Prihod')
async def key_start_prihod(message: types.Message):
    await message.answer('Тут треба вібрати від кого будуть поступати кошти:', reply_markup=keypad_prihod)


@dp.message_handler(text='Rashod')
async def key_start_rashod(message: types.Message):
    await message.answer('Тут треба вібрати группу на яку були трати:', reply_markup=keypad_rashod)


@dp.message_handler(text='Info')
async def key_start_info(message: types.Message):
    await message.answer('Інформація по фінансам\n'
                         'за поточний місяць ')


@dp.message_handler(text='Надходження\nАнна')
async def key_prihod_anna(message: types.Message):
    await message.answer('Вкажіть суму надходжень:\n'
                         '(сумму вкажіть без копійок)')


@dp.message_handler(text='Надходження\nСаша')
async def key_prihod_sasha(message: types.Message):
    await message.answer('Вкажіть суму надходжень:\n'
                         '(сумму вкажіть без копійок)')


@dp.message_handler(text='Назад да стартового меню')
async def key_prihod_back(message: types.Message):
    await message.answer(text='Back', reply_markup=keypad_start)