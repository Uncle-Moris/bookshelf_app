import psycopg2


sql = open("../migrations/01.sql").read()


class DB_Comunication:
    @staticmethod
    def connection(query):
        with psycopg2.connect(
                host="localhost",
                database = 'bookshelf',
                user = 'postgres',
                password = 'Admin1')\
                as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()


