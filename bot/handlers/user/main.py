from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.database.models import User
from bot.misc.util import langs

def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers
    dp.message.register(cmd_start_handler, CommandStart())


async def cmd_start_handler(msg: Message) -> None:  # Пользователь нажал на старт
    user = User(msg.from_user.id)
    await msg.answer(langs[user.language()]["start_msg"])
    if user.is_new():
        parameters = {
            'username': msg.from_user.username,
            'first_name': msg.from_user.first_name,
            'last_name': msg.from_user.last_name,
            'language': msg.from_user.language_code
        }
        user.add_user(parameters)
        await msg.answer(langs[user.language()]["start_msg_new"])
    else:
        await msg.answer(langs[user.language()]["start_msg_old"])

