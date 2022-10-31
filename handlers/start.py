from datetime import datetime, timezone
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from dateutil import tz

from keyboards.inline import registration
from loader import dp, db
from data import Inputs


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    user_ID = message.from_user.id
    result = await db.check_user(user_ID)
    if not result:
        
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text=f'Hello, {message.from_user.full_name}!\n'
                                       f'For access to more command use\n'
                                       f'/tools\n'
                                       f'\n'
                                       f'If you wanna collect records about your events\n'
                                       f'please push the registration button bellow:\n', reply_markup=registration)
        await Inputs.ChangeTimezone.set()
    else:
        user_rowid = await db.user_rowid(user_ID=message.from_user.id)
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text=f'Hello, {message.from_user.full_name}!\n'
                                       f'You are already listed in the database\n'
                                       f'Record <b>#{user_rowid}</>\n')


# @dp.message_handler(state=Inputs.ChangeTimezone)
# async def current_hour(message: types.Message):
#     await dp.bot.send_message(chat_id=message.from_user.id,
#                               text=f'For correct work among different timezones,\n'
#                                    f'please enter current hour (Format: HH, from 00 to 23)')
#     await Inputs.Registration.set()


@dp.message_handler(state=Inputs.Registration)
async def timestampcheck(message: types.Message, state: FSMContext):
    client_answer = message.text
    utc_hour = datetime.utcnow().hour
    client_time = int(str(client_answer[:2]))
    server_time = datetime.now().hour
    user_timezone = client_time - utc_hour
    await db.add_user(user_ID=message.from_user.id, username=message.from_user.username, current_timezone=user_timezone)
    user_timezone = '+' + str(user_timezone) if user_timezone >= 0 else str(user_timezone)
    user_rowid = await db.user_rowid(user_ID=message.from_user.id)
    await message.answer(f'your timezone is UTC{user_timezone}\n'
                         f'Now you are listed in DB, record number: {user_rowid}')

    await state.reset_state()
