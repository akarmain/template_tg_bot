from aiogram import Bot
from aiogram.types import BotCommand
from bot.misc.util import langs

async def set_my_commands(bot: Bot):
    for lang_code, lang_data in langs.items():
        commands = [
            BotCommand(command=name_cmd, description=desc)
            for name_cmd, desc in lang_data["edit_commands"].items()
        ]
        await bot.set_my_commands(commands, language_code=lang_code)


async def set_name_bot(bot: Bot):
    for lang_code, lang_data in langs.items():
        await bot.set_my_name(lang_data["edit_name"], language_code=lang_code)


async def set_description(bot: Bot):
    for lang_code, lang_data in langs.items():
        await bot.set_my_description(lang_data["edit_description"], language_code=lang_code)


async def set_short_description(bot: Bot):
    for lang_code, lang_data in langs.items():
        await bot.set_my_short_description(lang_data["edit_about"], language_code=lang_code)


async def set_me(bot: Bot):
    await set_name_bot(bot)
    await set_description(bot)
    await set_short_description(bot)
    await set_my_commands(bot)
