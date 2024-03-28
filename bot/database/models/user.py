from datetime import datetime

import bot.database as db
from bot.misc.util import ALL_LANGUAGE_CODES

language_cach = {}


class User:
    def __init__(self, user_id: int):
        self.u_id = user_id

    def add_user(self, parameters) -> None:
        """
        Добавляет пользователя в БД, необходимо передать словарь параметров
        :param parameters: {'username': -,
                            'first_name': -,
                            'last_name': -,
                            'language': -}
        """
        connection_time = datetime.now().strftime('%H:%M %d.%m.%Y')
        if db.get_user_exists(self.u_id):  # Ранее пользовался ботом, но заблокировал и бот это заметил
            db.update_now_use(self.u_id, 1) # Изменяет параметр
            db.update_connection_time(self.u_id, connection_time)
        else:
            language = self.language(parameters['language'])
            user_info = (self.u_id, f"@{parameters["username"]}", str(parameters["first_name"]), str(parameters["last_name"]),
                         language, str(parameters["language"]), connection_time, 0, 1, "-")
            db.main_set("users", *user_info)

    def language(self, first_language=None):
        if self.u_id in language_cach:
            return language_cach[self.u_id]
        elif not self.is_new():
            language = db.get_user_data(self.u_id, "language")[0][0]
            language_cach[self.u_id] = language
            return language
        elif first_language in ALL_LANGUAGE_CODES:
            language_cach[self.u_id] = first_language
            return first_language
        language_cach[self.u_id] = "en"
        return "en"

    def is_new(self):
        """
        Пользовался ли user ботом или заблокировал
        :return: True - да, False - нет
        """
        try:
            return db.get_user_data(self.u_id, "now_use")[0][0] != 1
        except Exception:
            return True
