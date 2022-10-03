from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

general_operations = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                           [
                                               InlineKeyboardButton(text='🕛 days counter', callback_data='button1')

                                           ],
                                           [
                                               InlineKeyboardButton(text='🗓️ date calculator', callback_data='button2')
                                           ],
                                       ])
