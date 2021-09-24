from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command('test'), user_id=[370912284, 463061743])
async def enter_test(message: types.Message):
    await message.answer('test \nРеши задачку\n10 + 10 * 10 - 10 = ?\n')

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '-80':
        await message.answer('Ok. are you sure? ')
    else:
        await message.answer('think again')
    await state.update_data(answer1=answer)
    # async with state.proxy() as data:
    #     data['answer1'] = answer

    await message.answer('Test2')
    # await Test.next()
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text

    await message.answer(' get answer{} and {}'.format(answer1, answer2))

    await state.finish()
    await state.reset_state(with_data=False)
