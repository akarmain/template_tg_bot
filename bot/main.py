from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from bot.handlers.main import register_all_handlers
from bot.misc import *
# from bot.utils.set_me import set_me


async def in_start(bot: Bot):
    # await set_me(bot)
    print("Aiogram bot is running")


async def in_stop():
    print("Aiogram bot is stopped")


async def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.startup.register(in_start)
    dp.shutdown.register(in_stop)
    register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
