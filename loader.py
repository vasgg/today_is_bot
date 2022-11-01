from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from db.aiosqlite import Database

import config

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', retention='30 days', enqueue=True)
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
db: Database = Database()
