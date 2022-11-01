import dateutil.parser
from handlers.start import registration
from handlers.states import Inputs
from loader import dp, db
from aiogram import types
from aiogram.dispatcher.filters import Command
from datetime import datetime
from calendar import monthrange


@dp.message_handler(Command('today_is'))
async def today_is(message: types.Message):
    today = datetime.now()
    current_year = datetime.now().year
    current_month = datetime.now().month
    dayofweek = today.strftime('%A')
    dayofmonth = today.strftime('%d')
    dayofyear = today.strftime('%j')
    yearprogress = int(today.strftime('%j')) / 365 * 100
    monthprogress = int(today.strftime('%d')) / monthrange(current_year, current_month)[1] * 100
    month = today.strftime('%B')
    year = today.strftime('%Y')
    numberofweeks = today.strftime('%V')
    registration_date = await db.registration_date(user_ID=message.from_user.id)
    user_ID = message.from_user.id
    result = await db.check_user(user_ID)
    days_sice_registration = dateutil.parser.parse(registration_date) - today
    if result:
        user_timezone = await db.user_timezone(user_ID=message.from_user.id)

        user_timezone = '+' + str(user_timezone) if user_timezone >= 0 else str(user_timezone)
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text=f'{dayofweek}, {dayofmonth}, {month} (month progress: {round(monthprogress)}%)\n'
                                       f'{dayofyear} day of {year} (year progress: {round(yearprogress)}%)\n'
                                       f'Week: {numberofweeks}\n'
                                       f'You listed in DB since {registration_date[0:10]} ({days_sice_registration.days + 1} days)\n'
                                       f'Your timezone is: UTC{user_timezone}\n'
                                       # f'ты зарегался в базе {} дней назад\n'  --- Тут надо прикрутить считывание с таблицы Records
                                       f'\n'
                                       f'if you want to change timezone use /settings command')
    else:
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text=f'{dayofweek}, {dayofmonth}, {month} (month progress: {round(monthprogress)}%)\n'
                                       f'{dayofyear} day of {year} (year progress: {round(yearprogress)}%)\n'
                                       f'\n'
                                       f'\n'
                                       f'Registered users have access to more features.\n'
                                       f'If you wanna join, push the button bellow:\n', reply_markup=registration)
        await Inputs.ChangeTimezone.set()

