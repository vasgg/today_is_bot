from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
from handlers.states import States
from loader import dp

help_commenmd_message = (f'For understanding supported input formats\n'
                         f'take a look at following examples:\n'
                         f'\n'
                         f'20 April 2000\n'
                         f'Apr 20 2000\n')


@dp.message_handler(Command('help'), state=States.all_states)
# @dp.message_handler(Command('help'), state=States.all_states)
async def help_command(message: types.Message, state: FSMContext):
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=help_commenmd_message)
    # f'<i>With questions, suggestions or feedback</>\n'
    # f'<i>please contact @vas1stdas.</>\n')
    # Это нужно поглубже убрать... Или вообще...


@dp.message_handler(Command("help"))
async def help_command(message: types.Message):
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=help_commenmd_message)

#  как бы мне не переписывать 2 раза этот код?
