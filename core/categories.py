from connections import ConnectionToDatabase


class Categories:
    def __init__(self, name):
        self.name = name

    def add_category(self):
        ConnectionToDatabase(
            'INSERT INTO categories (name) values (%s)',
            (self.name))

