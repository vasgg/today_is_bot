from datetime import datetime
import dateutil.parser
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, db
from handlers.states import States

registation_button = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='📔 registration', callback_data='registration')]])


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    user_ID = message.from_user.id
    result = await db.check_user(user_ID)
    if not result:
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text=f'Greetings, {message.from_user.full_name}.\n'
                                       f"Let's begin with <b>/today_is</> command\n"
                                       f'\n'
                                       f'For more opportunities push\n'
                                       f'<b>/tools</>\n'
                                       f'\n'
                                       f'If you wanna collect records about your events\n'
                                       f'please push the registration button bellow:\n', reply_markup=registation_button)

        await States.ChangeTimezone.set()
    else:
        today = datetime.now()
        user_rowid = await db.user_rowid(user_ID=message.from_user.id)
        registration_date = await db.registration_date(user_ID=message.from_user.id)
        days_sice_registration = dateutil.parser.parse(registration_date) - today
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text=f'Greetings, {message.from_user.full_name}!\n'
                                       f'You are listed in the database already.\n'
                                       f'Registration record <b>#{user_rowid}</>\n'
                                       f'Date of commit: {registration_date[0:10]} ({days_sice_registration.days + 1} days ago)\n')


@dp.callback_query_handler(text='registration', state=States.ChangeTimezone)
async def current_hour(message: types.Message):
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=f'For correct work with different timezones,\n'
                                   f'please enter current hour from your local timezone\n'
                                   f'(Format: HH, from 00 to 23)')
    await States.Registration.set()


@dp.message_handler(state=States.Registration)
async def registration(message: types.Message, state: FSMContext):
    client_answer = message.text
    utc_hour = datetime.utcnow().hour
    client_time = int(str(client_answer[:2]))
    user_timezone = client_time - utc_hour
    await db.add_user(user_ID=message.from_user.id, username=message.from_user.username, current_timezone=user_timezone)
    await db.registration_record(event_timestamp=datetime.utcnow(), event_name='date of registration',
                                 user_ID=message.from_user.id)
    user_timezone = '+' + str(user_timezone) if user_timezone >= 0 else str(user_timezone)
    user_rowid = await db.user_rowid(user_ID=message.from_user.id)
    await message.answer(f'Now you are listed in database (<b>user #{user_rowid}</>)\n'
                         f'\n'
                         f'Your timezone is <b>UTC{user_timezone}</>\n')
    # f'\n'
    # f'To change timezone you can use <b>/settings</> command')

    await state.reset_state()
