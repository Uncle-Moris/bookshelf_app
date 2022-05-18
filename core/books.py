import connections
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
    pass

