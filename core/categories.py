from connections import ConnectionToDatabase


class Categories:

    @staticmethod
    def add_new_category(name: str):
        ConnectionToDatabase.connection(
            'INSERT INTO public.categories(name) values (%s)', (name, ))

    @staticmethod
    def list_of_all_categories():
        ConnectionToDatabase(
            "SELECT * FROM public.categories",
            ())


Categories.add_new_category('Horror')
