from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
from handlers.states import Inputs
from loader import dp


@dp.message_handler(Command('help'), state=Inputs.all_states)
async def help_command(message: types.Message, state: FSMContext):
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=f'For understanding supported input formats\n'
                                   f'take a look at following examples:\n'
                                   f'\n'
                                   f'04.20.2000\n'
                                   f'04/20/2000:\n'
                                   f'20 April 2000\n'
                                   f'Apr 20 2000\n'
                                   f'\n')
    # f'<i>With questions, suggestions or feedback</>\n'
    # f'<i>please contact @vas1stdas.</>\n')
    # Это нужно поглубже убрать... Или вообще...


@dp.message_handler(Command("help"))
async def help_command(message: types.Message):
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=f'For understanding supported input formats\n'
                                   f'take a look at the following examples:\n'
                                   f'\n'
                                   f'04.20.2000\n'
                                   f'04/20/2000:\n'
                                   f'04202000\n'
                                   f'20 April 2000\n'
                                   f'Apr 20 2000\n'
                                   f'\n')

#  как бы мне не переписывать 2 раза этот код?
