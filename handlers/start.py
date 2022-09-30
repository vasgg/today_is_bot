from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=f'Hello, {message.from_user.full_name}!\n'
                                   f'This is @onem0redaybot\n'
                                   f'For access  to more command use\n'
                                   f'/today\n'
                                   f'/commands\n')

