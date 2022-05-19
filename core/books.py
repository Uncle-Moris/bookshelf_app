from connections import ConnectionToDatabase
from status import Status
import datetime

class Book:
    def __init__(self,
                 title: str,
                 author_id: int,
                 status_id: int,
                 published_at: datetime.date,
                 categories_id: int):
        self.title = title
        self.authors_id = author_id
        self.status_id = status_id
        self.published_at = published_at
        self.categories_id = categories_id


class BooksManaging:
    @staticmethod
    def add_book():
        title = input('Put a book title')
        #try:
        author_fullname = input("Put author fullname")
        author_fullname = author_fullname.split(' ')

        author_id = ConnectionToDatabase.select_all(
            f"select id"
            f" from public.authors "
            f"where first_name "
            f"ilike '%{author_fullname[0]}%' "
            f"and "
            f"last_name "
            f"ilike '%{author_fullname[1]}%' "
            f"limit 1", None)

        status_name = input('Put staust name')
        status_id = ConnectionToDatabase.select_all(
            f"SELECT id "
            f"FROM public.status "
            f"WHERE name "
            f"ilike '{status_name}' "
            f"LIMIT 1", None)

        published_at = input()

    @staticmethod
    def get_book_details():
        title = input('Put books title')
        return ConnectionToDatabase.select_all(
            f"SELECT * from public.books WHERE title ilike {title}"
        , None)
