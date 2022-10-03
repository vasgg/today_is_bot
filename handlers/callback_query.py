from datetime import datetime

import dateutil.parser
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import types

import data
from data import Inputs
from loader import dp


@dp.callback_query_handler(text=['button1', 'button2'])
async def days_operations(call: types.CallbackQuery):
    if call.data == 'button1':
        await Inputs.Counter.set()
        await call.message.answer('Enter your event date:')
        await call.answer()

    if call.data == 'button2':
        await Inputs.First_date.set()
        await call.message.answer('Enter the first date:')
        await call.answer()


@dp.message_handler(state=Inputs.Counter)
async def counter_input(message: types.Message, state: FSMContext):
    date_for_count = message.text
    # await state.update_data(input1=date_for_count)
    now = datetime.now()
    date1 = dateutil.parser.parse(date_for_count)
    period = now - date1
    if now.day == date1.day and now.month == date1.month and now.year == date1.year:
        await message.answer(f'Your date is today')
    elif now > date1:
        await message.answer(f'Your event was {period.days} days ago')
    else:
        period = date1 - now
        await message.answer(f'{int(period.days) + 1} days left until you event')
    await state.reset_state(with_data=False)


@dp.message_handler(state=Inputs.First_date)
async def counter_input(message: types.Message, state: FSMContext):
    first_date = message.text
    date1 = dateutil.parser.parse(first_date)
    await state.update_data(input1=date1)
    await message.answer(f'Enter the second date:')
    await Inputs.Second_date.set()


@dp.message_handler(state=Inputs.Second_date)
async def counter_input(message: types.Message, state: FSMContext):
    second_date = message.text
    now = datetime.now()
    date2 = dateutil.parser.parse(second_date)
    mydata = await state.get_data()
    date1 = mydata.get('input1')

    period = date2 - date1
    if date1.day == date2.day and date1.month == date2.month and date1.year == date2.year:
        await message.answer(f'Zero days between this dates')
    elif date2 > date1:
        await message.answer(f'{period.days} days between the dates')
    else:
        period = date1 - date2
        await message.answer(f'{period.days} days between the dates')
    await state.reset_state(with_data=False)
