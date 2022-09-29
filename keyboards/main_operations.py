from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_operations = InlineKeyboardMarkup(row_width=1,
                                           inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(text='🗓️ Today is', callback_data='button1')

                                               ],
                                               [
                                                   InlineKeyboardButton(text='🕛 How much days', callback_data='button2')
                                               ],
                                           ])
