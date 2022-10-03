from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from datetime import datetime
from calendar import monthrange

from dateutil import tz


@dp.message_handler(Command('today_is'), state=None)
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
    local_timezone = str(datetime.now(tz=tz.tzlocal()))
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=f'{dayofweek}, {dayofmonth}, {month} (month progress: {round(monthprogress)}%)\n'
                              # f'Month progress: {round(monthprogress)}%\n'
                              f'{dayofyear} day of {year} (year progress: {round(yearprogress)}%)\n'
                              # f'Year progress: {round(yearprogress)}%\n'
                              f'Week: {numberofweeks}\n'
                              f'Your timezone is: UTC{local_timezone[-6:]}\n')
