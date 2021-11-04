from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()


class AddingData(StatesGroup):
    D1 = State()
    D2 = State()
    Kvarplata = State()
    Products = State()
    OtherText = State()
    OtherInt = State()
