from os import environ
from typing import Final
from bot.misc.util import MY_BOT


class TgKeys:
    TOKEN: Final = environ.get('BOT_TG_TOKEN')


if __name__ == "__main__":
    ...
