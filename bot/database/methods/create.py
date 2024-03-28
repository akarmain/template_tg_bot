from bot.database.methods import *


def create_table_users() -> None:
    """
    Функция для создания таблицы "users" в БД.
    """
    with sq.connect(PATH_BAZE) as con:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS "users" (
         "u_id" INTEGER,
         "username" TEXT,
         "first_name" TEXT,
         "last_name" TEXT,
         "language" TEXT,
         "first_language" TEXT,
         "connection_time" TEXT,
         "operations_done" INTEGER,
         "now_use" INTEGER,
         "premium_end" TEXT
        );
        """

        cur = con.cursor()
        cur.execute(create_table_query)
        con.commit()


if __name__ == '__main__':
    create_table_users()
