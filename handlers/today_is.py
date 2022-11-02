import dateutil.parser
from handlers.start import registration, registation_button
from handlers.states import States
from loader import dp, db
from aiogram import types
from aiogram.dispatcher.filters import Command
from datetime import datetime
from calendar import monthrange

today = datetime.now()
current_year = datetime.now().year
current_month = datetime.now().month
dayofweek = today.strftime('%A')
dayofmonth = today.strftime('%-d')
dayofyear = today.strftime('%j')
yearprogress = round(int(today.strftime('%j')) / 365 * 100)
monthprogress = round(int(today.strftime('%d')) / monthrange(current_year, current_month)[1] * 100)
month = today.strftime('%B')
year = today.strftime('%Y')
numberofweeks = today.strftime('%V')

today_is_text = (f'<b>Today is:</>\n'
                 f'\n'
                 f'{dayofweek}, {dayofmonth} {month} (month progress: {monthprogress}%)\n'
                 f'Day #{dayofyear} of {year} (year progress: {yearprogress}%)\n'
                 f'Week #{numberofweeks}\n')


@dp.message_handler(Command('today_is'))
async def today_is(message: types.Message):
    user_ID = message.from_user.id
    result = await db.check_user(user_ID)
    if result:
        registration_date = await db.registration_date(user_ID=message.from_user.id)
        registration_date_obj = dateutil.parser.parse(registration_date)
        days_sice_registration = today - dateutil.parser.parse(registration_date)
        user_timezone = await db.user_timezone(user_ID=message.from_user.id)
        user_timezone = '+' + str(user_timezone) if user_timezone >= 0 else str(user_timezone)
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text='\n'.join([today_is_text,
                                                  f'You registered {days_sice_registration.days} days ago, '
                                                  f'{registration_date_obj.strftime("%-d %B %Y")}',
                                                  f'Local timezone: UTC{user_timezone}']))
        # f'\n'
        # f'if you want to change timezone use /settings command')
    else:
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  reply_markup=registation_button,
                                  text='\n'.join(
                                      [today_is_text,
                                       'Registered users have access to more features', 'If you wanna join, push the button bellow:']))
        await States.ChangeTimezone.set()
