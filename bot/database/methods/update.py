from bot.database.methods import *


def main_set(table: str, *args) -> None:
    """
    Главная функция для добавления информации в БД

    :param table: Таблица куда будем добавлять
    :param args: Значение каждой ячейки
    :return: None
    """
    with sq.connect(PATH_BAZE) as con:
        placeholders = ', '.join(['?'] * len(args))
        sql_query = f"INSERT INTO {table} VALUES({placeholders})"
        con.executemany(sql_query, [args])


def update_now_use(u_id, value):
    with sq.connect(PATH_BAZE) as con:
        sql_query = f'UPDATE "users" SET "now_use" = ? WHERE "u_id" = ?'
        cur = con.cursor()
        cur.execute(sql_query, (value, u_id))


def update_connection_time(u_id, new_connection_time):
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        cur.execute('SELECT "connection_time" FROM "users" WHERE "u_id" = ?', (u_id,))
        existing_time = cur.fetchone()
        updated_time = existing_time[0] + "\n" + new_connection_time
        cur.execute(
            'UPDATE "users" SET "connection_time" = ? WHERE "u_id" = ?',
            (updated_time, u_id)
        )
    con.commit()
