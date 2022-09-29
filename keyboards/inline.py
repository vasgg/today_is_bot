from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

today_button = InlineKeyboardButton(text='🗓️ Today is', callback_data='button1'),
days_counter = InlineKeyboardButton(text='🕛 How much days', callback_data='button2')

# main_commands = InlineKeyboardMarkup().add(button1, button2)
# main_commands = InlineKeyboardMarkup(row_width=1, inline_keyboard=[[today_button], [days_counter]])

main_commands = InlineKeyboardMarkup()

main_commands.insert(today_button)
main_commands.insert(days_counter)

