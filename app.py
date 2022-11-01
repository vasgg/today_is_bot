from aiogram.utils import executor


from handlers import dp
from loader import db, logger


async def on_startup(dp):
    """
    Корутина создает бд Users и устанавливает
    меню команд бота при запуске модуля app.py
    :param dp: объект класса Dispatcher отлавливает все обновления от API телеграм
    """

    try:
        await db.create_table_users()
        await db.create_table_records()

    except Exception as e:
        # logger.error(str(type(e)), str(e))
        pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
