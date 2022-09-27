from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command("commands"))
async def commands_command(message: types.Message):
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text='This bot allows you count days between dates')


