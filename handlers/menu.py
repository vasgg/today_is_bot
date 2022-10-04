from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from keyboards.main_operations import general_operations
from loader import dp


@dp.message_handler(Command("tools"))
async def commands(message: types.Message):
    await message.answer(text='This bot allows you count days between dates', reply_markup=general_operations)


