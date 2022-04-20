import psycopg2


sql = open("../migrations/initial_db_script.sql").read()


class DB_Comunication:
    @staticmethod
    def connection(query):
        with psycopg2.connect(
                port='5050',
                host="localhost",
                database = 'bookshelf_app',
                user = 'bookshelf_app',
                password = 'password')\
                as conn:
            with conn.cursor() as cur:
                cur.execute(query)
            conn.commit()


DB_Comunication().connection(sql)