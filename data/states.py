from aiogram.dispatcher.filters.state import StatesGroup, State


class Inputs(StatesGroup):
    Counter = State()
    Calculator = State()
    First_date = State()
    Second_date = State()
    Registration = State()
    ChangeTimezone = State()
