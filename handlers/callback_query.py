# from datetime import datetime, timezone
# from calendar import monthrange
# from tzlocal import get_localzone
# from aiogram import types
# from dateutil import tz
#
# from loader import dp
#

#
# @dp.callback_query_handler(text=['button1', 'button2'])
# async def today_is(call: types.CallbackQuery):
#     if call.data == 'button1':
        # today = datetime.now()
        # current_year = datetime.now().year
        # current_month = datetime.now().month
        # dayofweek = today.strftime('%A')
        # dayofmonth = today.strftime('%d')
        # dayofyear = today.strftime('%j')
        # yearprogress = int(today.strftime('%j')) / 365 * 100
        # monthprogress = int(today.strftime('%d')) / monthrange(current_year, current_month)[1] * 100
        # month = today.strftime('%B')
        # year = today.strftime('%Y')
        # numberofweeks = today.strftime('%V')
        # LOCAL_TIMEZONE = str(datetime.now(tz = tz.tzlocal()))
        # await call.message.answer(f'Today is: {dayofweek}, {dayofmonth} day of {month}\n'
        #                           f'{dayofyear} day of {year}\n'
        #                           f'Year progress: {round(yearprogress)}%\n'
        #                           f'Week №: {numberofweeks} / 52\n'
        #                           f'Month progress: {round(monthprogress)}%\n'
        #                           f'Your timezone is: UTC{LOCAL_TIMEZONE[-6:]}\n')

    # if call.data == 'button2':
    #     await call.message.answer('Enter your event date:')
    # await call.answer()
