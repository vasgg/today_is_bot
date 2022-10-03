from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command("help"))
async def start_command(message: types.Message):
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=f'I hope you enjoy this bot!\n'
                                   f'This is my very first personal python project.\n'
                                   f'With questions, suggestions or feedback\n'
                                   f'you can contact @vas1stdas.\n'
                                   f'Please, share this bot with your friends.\n')
