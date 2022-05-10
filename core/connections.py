"""This module is responsible for connecting witch project database"""
import psycopg2


class ConnectionToDatabase:
    """Object responsible for db connection"""
    @staticmethod
    def connection(query: str, values: tuple = None):
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
