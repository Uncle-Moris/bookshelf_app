"""This module is responsible for connecting witch project database"""
import psycopg2

DATES_TO_CONNECTION = dict(
                port='5050',
                host="localhost",
                database='bookshelf_app',
                user='bookshelf_app',
                password='password')

class ConnectionToDatabase:
    """Class responsible for db connection"""

    @staticmethod
    def connection(query: str, values: tuple):
        """Database connection"""
        with psycopg2.connect(
                port='5050',
                host="localhost",
                database='bookshelf_app',
                user='bookshelf_app',
                password='password')\
                as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
            conn.commit()

    @staticmethod
    def select_all(query: str, values: tuple = None):
        with psycopg2.connect(
                port='5050',
                host="localhost",
                database='bookshelf_app',
                user='bookshelf_app',
                password='password') \
                as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
                return cur.fetchall()


            #conn.commit()

