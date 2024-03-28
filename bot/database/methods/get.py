from typing import List, Any
from bot.database.methods import *


def get_user_data(id, cell: str = "*") -> list[Any]:
    """
    1 функция для получения значений из БД
    :param cell:  Значение которое хотим полуить

    :return: Значение из БД
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        res = cur.execute(f'SELECT {cell} FROM "users" WHERE "u_id" = ?', (id,))
        return res.fetchall()


def get_user_exists(u_id) -> bool:
    """
    Функция проверяет существует ли пользователь в базе данных.
    :param id: Идентификатор пользователя для проверки.
    :return: True если пользователь существует, иначе False.
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        cur.execute(f'SELECT "u_id" FROM "users" WHERE "u_id" = ?', (u_id,))
        return bool(cur.fetchone())

