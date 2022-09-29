from datetime import datetime as dt

from aiogram import types
from dateutil.utils import today

from loader import dp
# from dateutil.parser import parse
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *


@dp.callback_query_handler(text=['button1', 'button2'])
async def today_is(call: types.CallbackQuery):
    if call.data == 'button1':
        today = datetime.today()
        # dt_st7ring = dt.strftime("Date: %d/%m/%Y  time: %H:%M:%S")
        await call.message.answer(f"Today is: {today}")
    if call.data == 'button2':
        await call.message.answer('Enter your event date:')
